#!/usr/bin/env python3
"""SHED 2024→2025 Household Maintenance Transition Gate v0.1.1

Reads the official Federal Reserve SHED 2024 and 2025 CSV ZIP files,
links repeat respondents on `shedid`, uses the 2025 `panel_weight`, and tests
whether 2024 payment status alone is predictively closed with respect to a
2025 three-state bill outcome, or whether 2024 buffer coordinates materially
change successor-state laws.

Outputs CSV/JSON results into --out.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import log_loss
except Exception as e:
    raise SystemExit("scikit-learn is required for the predictive gate") from e


def read_first_csv(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, low_memory=False)
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as zf:
            csvs = [n for n in zf.namelist() if n.lower().endswith('.csv') and not n.startswith('__MACOSX/')]
            if not csvs:
                raise ValueError(f"No CSV found in {path}")
            # Prefer a data-looking file if the archive contains documentation CSVs too.
            csvs.sort(key=lambda n: (0 if ('public' in n.lower() or 'shed' in n.lower()) else 1, len(n)))
            with zf.open(csvs[0]) as f:
                return pd.read_csv(f, low_memory=False)
    raise ValueError(f"Expected .csv or .zip, got {path}")


def cmap(df: pd.DataFrame) -> dict[str, str]:
    return {str(c).lower(): str(c) for c in df.columns}


def col(df: pd.DataFrame, name: str) -> pd.Series:
    m = cmap(df)
    key = name.lower()
    if key not in m:
        raise KeyError(f"Missing required variable {name}; case-insensitive search failed")
    return df[m[key]]


def binary01(s: pd.Series) -> pd.Series:
    """Normalize SHED Yes/No public-use encodings (or numeric 1/0) to floats."""
    if pd.api.types.is_numeric_dtype(s):
        return pd.to_numeric(s, errors='coerce')
    x = s.astype('string').str.strip()
    return x.map({'Yes':1.0, 'No':0.0, '1':1.0, '0':0.0})


def monthend_score(s: pd.Series) -> pd.Series:
    """Normalize B1_a to the frozen favorable-margin scale."""
    if pd.api.types.is_numeric_dtype(s):
        return pd.to_numeric(s, errors='coerce').map({1:1.0,2:.75,3:.5,4:.25,5:0.0})
    x = s.astype('string').str.strip()
    return x.map({'Always':1.0,'Often':.75,'Sometimes':.5,'Rarely':.25,'Never':0.0})


def wmean(mask: np.ndarray, w: np.ndarray) -> float:
    mask = np.asarray(mask, dtype=float)
    w = np.asarray(w, dtype=float)
    good = np.isfinite(mask) & np.isfinite(w)
    if not good.any() or w[good].sum() <= 0:
        return float('nan')
    return float(np.sum(mask[good] * w[good]) / np.sum(w[good]))


def weighted_state_dist(y: np.ndarray, w: np.ndarray, classes=(0,1,2)) -> np.ndarray:
    out = []
    denom = np.sum(w[np.isfinite(w)])
    if denom <= 0:
        return np.full(len(classes), np.nan)
    for c in classes:
        out.append(np.sum(w[(y == c) & np.isfinite(w)]) / denom)
    return np.asarray(out, float)


def tv(p: np.ndarray, q: np.ndarray) -> float:
    return 0.5 * float(np.nansum(np.abs(np.asarray(p)-np.asarray(q))))


def weighted_multiclass_logloss(y_true, p, w):
    # sklearn log_loss supports sample_weight.
    return float(log_loss(y_true, p, labels=[0,1,2], sample_weight=w))


def design_matrix(d: pd.DataFrame, extended: bool) -> np.ndarray:
    # Always include payment status. Extended model adds declared buffer coordinates.
    base = [d['p24_current'].to_numpy(float)]
    if extended:
        base.extend([
            d['r24_three_month'].to_numpy(float),
            d['r24_unable_400'].to_numpy(float),
            d['r24_monthend'].to_numpy(float),
        ])
    return np.column_stack(base)


def cv_logloss(d: pd.DataFrame, extended: bool, splits=10, seed=437) -> float:
    X = design_matrix(d, extended)
    y = d['y25'].to_numpy(int)
    w = d['panel_weight'].to_numpy(float)
    # Stable stratification across outcome states.
    skf = StratifiedKFold(n_splits=splits, shuffle=True, random_state=seed)
    total_num = 0.0
    total_den = 0.0
    for tr, te in skf.split(X, y):
        model = LogisticRegression(max_iter=3000, solver='lbfgs')
        model.fit(X[tr], y[tr], sample_weight=w[tr])
        p = model.predict_proba(X[te])
        # Ensure columns map to 0,1,2.
        pp = np.full((len(te), 3), 1e-15)
        for j, c in enumerate(model.classes_):
            pp[:, int(c)] = p[:, j]
        pp = pp / pp.sum(axis=1, keepdims=True)
        ll = weighted_multiclass_logloss(y[te], pp, w[te])
        total_num += ll * w[te].sum()
        total_den += w[te].sum()
    return total_num / total_den


def bootstrap_tv(d: pd.DataFrame, p_state: int, low_group: str='2+', high_group: str='0', reps=1000, seed=437):
    sub = d[d['p24_current'] == p_state].reset_index(drop=True)
    if sub.empty:
        return {'estimate': float('nan'), 'lo': float('nan'), 'hi': float('nan')}

    def one(x):
        a = x[x['depletion_group'] == high_group]
        b = x[x['depletion_group'] == low_group]
        if len(a) < 5 or len(b) < 5:
            return np.nan
        pa = weighted_state_dist(a.y25.to_numpy(), a.panel_weight.to_numpy())
        pb = weighted_state_dist(b.y25.to_numpy(), b.panel_weight.to_numpy())
        return tv(pa,pb)

    est = one(sub)
    rng = np.random.default_rng(seed + p_state)
    vals = []
    n = len(sub)
    for _ in range(reps):
        idx = rng.integers(0, n, size=n)
        vals.append(one(sub.iloc[idx]))
    vals = np.asarray(vals, float)
    vals = vals[np.isfinite(vals)]
    lo, hi = (np.quantile(vals,[.025,.975]) if len(vals) else (np.nan,np.nan))
    return {'estimate': float(est), 'lo': float(lo), 'hi': float(hi), 'bootstrap_reps_valid': int(len(vals))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--shed2024', required=True)
    ap.add_argument('--shed2025', required=True)
    ap.add_argument('--out', default='shed_transition_results_v0_1')
    ap.add_argument('--bootstrap', type=int, default=1000)
    args = ap.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    d24 = read_first_csv(args.shed2024)
    d25 = read_first_csv(args.shed2025)

    # Rename only required columns into a stable internal schema.
    a24 = pd.DataFrame({
        'shedid': col(d24,'shedid').astype(str),
        'p24_current': binary01(col(d24,'EF5C')),
        'r24_three_month': binary01(col(d24,'EF1')),
        'r24_unable_400': binary01(col(d24,'EF3_h')),
        'b1a24': col(d24,'B1_a'),
    })
    a25 = pd.DataFrame({
        'shedid': col(d25,'shedid').astype(str),
        'panel_weight': pd.to_numeric(col(d25,'panel_weight'), errors='coerce'),
        'ef5c25': binary01(col(d25,'EF5C')),
        'ef5d25': binary01(col(d25,'EF5D')),
    })

    # The 2025 panel weight is defined for respondents who also took the 2024 SHED.
    a25 = a25[a25['panel_weight'].notna()].copy()
    d = a25.merge(a24, on='shedid', how='inner', validate='one_to_one')

    # 2025 successor state: 0 healthy/current-no-difficulty; 1 current-but-strained; 2 payment failure.
    y = np.full(len(d), np.nan)
    y[(d.ef5c25 == 1) & (d.ef5d25 == 0)] = 0
    y[(d.ef5c25 == 1) & (d.ef5d25 == 1)] = 1
    y[d.ef5c25 == 0] = 2
    d['y25'] = y

    # Favorable month-end margin score: Always=1, Often=.75, Sometimes=.5, Rarely=.25, Never=0.
    d['r24_monthend'] = monthend_score(d['b1a24'])
    d['bad_reserve'] = (d['r24_three_month'] == 0).astype(float)
    d['bad_400'] = (d['r24_unable_400'] == 1).astype(float)
    d['bad_monthend'] = (d['r24_monthend'] <= .25).astype(float)
    d['depletion_count'] = d[['bad_reserve','bad_400','bad_monthend']].sum(axis=1)
    d['depletion_group'] = pd.cut(d['depletion_count'], bins=[-0.1,.1,1.1,3.1], labels=['0','1','2+']).astype(str)

    required = ['panel_weight','p24_current','r24_three_month','r24_unable_400','r24_monthend','y25']
    analy = d.dropna(subset=required).copy()

    # Transition table by 2024 payment status and depletion group.
    rows=[]
    for p in [1,0]:
        for g in ['0','1','2+']:
            s=analy[(analy.p24_current==p)&(analy.depletion_group==g)]
            if len(s)==0:
                continue
            dist=weighted_state_dist(s.y25.to_numpy(), s.panel_weight.to_numpy())
            rows.append({
                'p24_current': int(p), 'depletion_group': g,
                'n_unweighted': int(len(s)), 'weight_sum': float(s.panel_weight.sum()),
                'p25_healthy': float(dist[0]), 'p25_current_strained': float(dist[1]), 'p25_payment_failure': float(dist[2])
            })
    trans=pd.DataFrame(rows)
    trans.to_csv(outdir/'transition_matrix.csv', index=False)

    # Closure diagnostic: TV distance between best-buffer (0) and depleted (2+) successor laws within same P24 label.
    tv_results={}
    for p in [1,0]:
        tv_results[str(p)] = bootstrap_tv(analy, p_state=p, reps=args.bootstrap)

    # Predictive gate: 10-fold weighted CV log loss.
    ll0 = cv_logloss(analy, extended=False)
    ll1 = cv_logloss(analy, extended=True)
    improvement = (ll0-ll1)/ll0 if ll0>0 else np.nan

    # Frozen evidence gate.
    # Payment-only closure fails diagnostically if, for at least one payment label,
    # TV >= .05 and the bootstrap 95% lower bound exceeds .01, OR extended features improve
    # weighted out-of-sample log loss by >= .5%.
    tv_gate = any(v.get('estimate',np.nan) >= .05 and v.get('lo',np.nan) > .01 for v in tv_results.values())
    pred_gate = bool(np.isfinite(improvement) and improvement >= .005)
    verdict = 'FAIL_PAYMENT_ONLY_CLOSURE' if (tv_gate or pred_gate) else 'NOT_ESTABLISHED'

    result = {
        'protocol':'SHED_2024_2025_MAINTENANCE_TRANSITION_GATE_v0.1',
        'n_2024': int(len(d24)),
        'n_2025': int(len(d25)),
        'n_2025_panel_weight_nonmissing': int(a25.shape[0]),
        'n_matched_panel': int(len(d)),
        'n_complete_analysis': int(len(analy)),
        'state_2025': {
            '0':'healthy/current-no-difficulty',
            '1':'current-but-strained',
            '2':'payment-failure'
        },
        'predictors_2024': ['EF5C payment status','EF1 three-month rainy-day fund','EF3_h unable to pay $400 now','B1_a month-end money margin'],
        'panel_weight':'2025 panel_weight',
        'tv_best_vs_depleted_by_2024_payment_state': tv_results,
        'weighted_10fold_logloss_payment_only': ll0,
        'weighted_10fold_logloss_payment_plus_buffers': ll1,
        'relative_logloss_improvement': float(improvement),
        'gates': {'tv_gate': bool(tv_gate), 'predictive_gate': bool(pred_gate)},
        'verdict': verdict,
        'interpretation_rule':'This is a predictive-closure diagnostic, not a causal model. A failure means 2024 payment label alone is not sufficient to equalize observed 2025 successor-state laws under the declared state/output definition.'
    }
    with open(outdir/'result.json','w') as f:
        json.dump(result,f,indent=2)
    analy[['shedid','panel_weight','p24_current','r24_three_month','r24_unable_400','b1a24','r24_monthend','depletion_count','depletion_group','y25']].to_csv(outdir/'panel_analysis_rows.csv',index=False)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

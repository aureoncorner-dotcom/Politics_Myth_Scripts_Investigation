# SHED 2024→2025 Household Maintenance Transition Gate — Result v0.1

**Run date:** 6 September 2026  
**Inputs:** Federal Reserve SHED public-use CSV ZIPs for 2024 and 2025 supplied in-chat  
**Frozen protocol:** `SHED_TRANSITION_PROTOCOL_v0.1.json`  
**Verdict:** **FAIL_PAYMENT_ONLY_CLOSURE**

## Implementation note

The frozen protocol and evidence gates were not changed. The original v0.1 runner expected numeric 0/1 encodings, while the official public-use CSVs encode the relevant binary variables as `Yes`/`No` and `B1_a` as text categories. Runner v0.1.1 adds only the required encoding normalization before executing the frozen analysis.

## Panel

- 2024 respondents: **12,295**
- 2025 respondents: **12,934**
- 2025 respondents with nonmissing panel weight: **4,419**
- Matched `shedid` panel: **4,419**
- Complete analysis cases: **4,419**

The 2025 successor state was frozen as:

- **0:** current, no difficulty
- **1:** current, but difficulty paying
- **2:** payment failure

The 2024 payment label was tested alone and then with three declared buffer coordinates: three-month rainy-day fund, ability to absorb the $400 shock, and month-end money margin.

## Primary transition result

Weighted 2025 successor-state law conditional on the same 2024 payment label:

| 2024 payment state | 2024 depletion group | n | Healthy 2025 | Current-but-strained 2025 | Payment failure 2025 |
|---|---|---:|---:|---:|---:|
| Current | 0 depleted buffers | 2,131 | **92.73%** | 3.24% | 4.03% |
| Current | 1 depleted buffer | 977 | 81.24% | 10.48% | 8.28% |
| Current | 2+ depleted buffers | 755 | **52.97%** | **25.39%** | **21.64%** |
| Not current | 0 depleted buffers | 75 | 67.15% | 13.52% | 19.33% |
| Not current | 1 depleted buffer | 133 | 44.43% | 10.75% | 44.83% |
| Not current | 2+ depleted buffers | 348 | 21.88% | 24.91% | 53.21% |

Among respondents who were **current in 2024**, moving from zero declared depleted buffers to two or more changes the weighted 2025 successor distribution by a total-variation distance of:

**TV = 0.3976; bootstrap 95% interval [0.3591, 0.4390].**

For respondents who were **not current in 2024**:

**TV = 0.4527; bootstrap 95% interval [0.3251, 0.5774].**

Both exceed the frozen TV gate (`TV >= 0.05` and lower bootstrap bound `> 0.01`).

### Current-in-2024 contrast

Within the same favorable 2024 payment label:

- 2025 payment failure rises from **4.03% → 21.64%** with 2+ depleted buffers (**5.37×**, +17.61 percentage points).
- Current-but-strained rises from **3.24% → 25.39%** (**7.83×**, +22.15 points).
- The combined strained-or-failed successor state rises from **7.27% → 47.03%** (**6.47×**, +39.76 points).
- Healthy/current-no-difficulty falls from **92.73% → 52.97%**.

This is the cleanest result in the run: **the 2024 payment label does not equalize the observed 2025 successor-state law once buffer depletion is resolved.**

## Predictive gate

Weighted 10-fold out-of-sample multiclass log loss:

- Payment status only: **0.66536**
- Payment + declared buffers: **0.58952**
- Relative improvement: **11.40%**

Frozen predictive threshold: **0.5%** relative improvement.

**Predictive gate: PASS by a wide margin.**

## Secondary decomposition (exploratory; not part of the frozen primary gate)

Relative 10-fold log-loss improvement over payment-only:

- + three-month reserve: **6.24%**
- + $400-shock coordinate: **4.20%**
- + month-end money margin: **8.58%**
- + all three buffers: **11.40%**

All three coordinates carry predictive information; the month-end margin is the strongest single addition in this simple model.

## Evidence status

**Supported by this run**

- Payment status alone is an empirically insufficient predictive state under the frozen 2024→2025 SHED transition diagnostic.
- Buffer coordinates materially change successor-state distributions among respondents sharing the same prior payment label.
- The refined state materially improves out-of-sample prediction of the three-state 2025 outcome.

**Not established by this run**

- Causality.
- A universal deterministic transition law.
- A claim that all U.S. household margin is collapsing.
- A claim that current-but-strained always precedes default.
- A claim that these three buffer coordinates are the unique or minimal sufficient state.

## Frozen verdict

> **FAIL_PAYMENT_ONLY_CLOSURE**
>
> Both preregistered gates fire. Under the declared SHED state/output definition, the coarse 2024 payment label is not an adequate autonomous predictive coordinate for the 2025 successor state. The buffer-refined state is empirically better.

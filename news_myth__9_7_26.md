# News-to-Myth Evidence Bridge v0.2

**Status:** working research protocol  
**License:** CC0 1.0 Universal — anonymous public-domain dedication; no rights reserved; no warranty  
**Purpose:** connect current-record research to functional comparison and fiction without allowing symbolism to become evidence

## The three-layer rule

```text
Layer A — public record
        ↓
Layer B — functional comparison
        ↓
Layer C — mythic / fictional adaptation
```

Evidence may move downward. It may not move backward.

- A mythic resemblance cannot prove a factual claim.
- Timing, proximity, shared associates, or aesthetic similarity cannot prove coordination.
- A functional comparison describes what a documented act does in a system; it does not identify a person with a god.
- Fiction may combine, exaggerate, invert, or invent roles only after its departures from the record are labeled.

## Layer A — atomic public-record ledger

One row holds one claim. Compound claims must be split.

| Field | Required content |
|---|---|
| Item ID | Stable identifier, such as `NEWS-2026-001` |
| Claim ID | Atomic child identifier, such as `NEWS-2026-001-C1` |
| Actor / institution | The participant actually named by the source |
| Event date | When the underlying act occurred |
| Publication / filing date | When the record became public |
| Primary source | Direct agency, court, disclosure, contract, or corporate filing link |
| Source role | Primary record / official characterization / secondary report / allegation / context |
| Exact public-record fact | Narrow statement directly supported by the cited source |
| Evidence status | Established record / agency conclusion / allegation / reasonable inference / unknown |
| Counterevidence | Record tending against or narrowing the claim |
| Missing link | Specific causal, authorization, knowledge, benefit, or participation link not established |
| Dependence cluster | Other claims relying on the same source, witness, or underlying event |
| Update state | New / materially updated / unchanged / corrected / withdrawn / superseded |
| Raw receipt | Saved URL, document ID, page or section, access date, and optional hash |

### Required claim labels

- **Established public-record fact:** the cited record directly establishes the narrow proposition.
- **Official or institutional conclusion:** an agency or organization states a conclusion; the existence of the conclusion is established, but its truth may remain contested.
- **Allegation:** a named source asserts the proposition without adjudication or sufficient independent confirmation.
- **Reasonable inference:** the known facts support the interpretation, but do not compel it.
- **Counterevidence:** evidence that contradicts, narrows, mitigates, or supplies an ordinary alternative explanation.
- **Missing link:** the exact step that would be needed to move from association or sequence to participation or causation.
- **Unknown:** the source record does not answer the question.

## Event lifecycle

Do not collapse these stages:

```text
DET — detected, announced, referred, or flagged
DEC — authorized, denied, deferred, recused, or otherwise decided
ACT — attempted or applied action, with the responsible executor identified
EFF — measured result, adverse consequence, reversal, rollback, or unresolved state
```

An announcement is not implementation. A referral is not enforcement. A policy is not an outcome. A detector crossing is not proof of a mechanism.

## Current actor / institution queue

This is a monitoring queue, not a guilt list and not a casting chart.

| Queue | Record families to prioritize | Participation question |
|---|---|---|
| Trump / World Liberty Financial and counterparties | OGE and presidential disclosures; OCC and SEC records; official corporate filings; clemency and executive records | What transaction, decision, disclosure duty, benefit, or counterparty link is documented? |
| Todd Blanche | DOJ releases; ethics agreements; recusals; digital-asset policy and enforcement records | Did Blanche authorize, participate, recuse, delegate, or merely hold an adjacent office? |
| Kash Patel / FBI / Palantir | FBI and DOJ releases; procurement records; USAspending; SAM; Inspector General and GAO material | Is a contract, task order, decision chain, deliverable, or personal participation link public? |
| Paula White-Cain / White House Faith Office | White House orders and releases; DOJ implementation records; grants and procurement | Is there a documented operational, funding, referral, or policy-implementation link? |
| Bondi, Gabbard, Hegseth, RFK Jr. | Ethics agreements; disclosures; recusals; agency actions; procurement and Inspector General records | Which act belongs to the official personally, the office generally, or a subordinate process? |
| Johnson, McConnell, federal judiciary, Supreme Court | Congressional and judicial disclosures; gifts; travel; recusals; opinions and orders | What duty, disclosure, case participation, or recusal decision is actually documented? |

## Layer B — functional comparison

Layer B begins only after the Layer A row is frozen. It compares documented functions, not souls, identities, secret motives, or divine essences.

| Comparator | Functional question | Failure mode to test | Evidence prohibition |
|---|---|---|---|
| Zeus | Does personal command override a general or reviewable rule? | Crown, exceptional authority, patronage | Status or power alone does not establish arbitrary command |
| Nomos | Who writes, interprets, changes, and is bound by the rule? | Rule capture, selective enforcement, compulsory interpreter | The existence of law does not establish neutral application |
| Pheme | How does repetition alter reputation, credibility, or the perceived record? | Rumor becoming evidence; signal capture | Virality and repetition do not establish truth |
| Ares | What coercive machinery is authorized or deployed? | Force substituting for adjudication | Aggressive rhetoric does not establish applied force |
| Eris | Who benefits from conflict, fragmentation, or mutually reinforcing hostility? | Conflict production, institutional splitting | Polarization does not by itself establish deliberate orchestration |
| Dolos | Was a material process designed to conceal, reroute, or induce reliance? | Procedural deception, concealed routing | Complexity, error, or opacity alone does not establish deceit |
| Apate | Was a materially false appearance knowingly presented as reality? | False front, misrepresentation | Inaccuracy alone does not establish knowledge or intent |
| Plutus | Where do money, ownership, access, contracts, or benefits move? | Wealth capture, dependency, purchased standing | Benefit or proximity alone does not establish quid pro quo |
| Pseudologoi | Are multiple false claims produced, repeated, or operationalized? | Industrialized falsehood, narrative flooding | A disputed statement is not automatically a knowing lie |

Multiple comparators may be active. Preserve the full profile; do not force a single winner.

## Layer C — fictional adaptation

Each story element receives one boundary label:

| Label | Meaning |
|---|---|
| `REC` | Closely derived from a cited public record |
| `CMP` | Functional comparison built from Layer A, not a literal identity claim |
| `SYN` | Synthetic composite assembled from more than one event or actor |
| `INV` | Project invention with no claim of historical or contemporary truth |

The fictional pantheon may therefore be brutal, funny, profane, composite, or impossible. Its freedom comes from keeping the seam visible.

## Single-item research card

```yaml
item_id: null
headline: null
event_date: null
publication_date: null
actors: []
primary_records: []

claims:
  - claim_id: null
    proposition: null
    source_role: null
    evidence_status: null
    support: []
    counterevidence: []
    missing_link: null
    dependence_cluster: null

lifecycle:
  detected: null
  decided: null
  attempted: null
  applied: null
  effect: null
  rollback_or_closure: null

functional_comparison:
  comparators: []
  documented_function: null
  alternative_read: null
  confidence: null

fiction_bridge:
  boundary_label: null
  scene_pressure: null
  transformation_or_invention: null
```

## Publication gate

Before a research item becomes a story seed, ask:

1. Is every factual sentence attached to a direct source or clearly labeled source role?
2. Are event date and publication date separate?
3. Are allegation, inference, counterevidence, and missing link visible?
4. Are detection, decision, action, and effect kept separate?
5. Could removal of one dependent source collapse several claims? If so, are they marked as one dependence cluster?
6. Is there a mundane explanation that remains live?
7. Does the mythic comparison describe a function rather than claim an identity?
8. Are all composites and inventions labeled before prose is drafted?

## Compact law

```text
source ≠ report ≠ inference ≠ action ≠ outcome ≠ myth

The record can inspire the myth.
The myth cannot certify the record.
```

## Frozen current-record cards

These cards were added on September 7, 2026. They preserve the factual and fictional layers separately and should be updated only when a primary record materially changes the stated lifecycle.

### NEWS-2026-001 — HHS funding priorities and conflicts of interest

- **Actor / institution:** U.S. Department of Health and Human Services; Secretary Robert F. Kennedy Jr. is identified on the page.
- **Publication / update date:** September 1, 2026.
- **Primary source:** [HHS Priorities](https://www.hhs.gov/about/priorities/index.html)
- **Raw receipt:** HHS page, sections “Prevent conflicts of interest” and introductory funding language; accessed September 7, 2026.
- **Lifecycle:** `DET` public announcement; `DEC` department-level priority stated; `ACT` no specific funding decision identified; `EFF` unknown.

| Claim ID | Status | Atomic proposition |
|---|---|---|
| `NEWS-2026-001-C1` | Established public-record fact | HHS states that it is adopting a unified strategy intended to align departmental priorities and funding. |
| `NEWS-2026-001-C2` | Established public-record fact | HHS states that it will deprioritize partnerships with organizations that present conflicts of interest, politicize science, or otherwise compromise objectivity or integrity in HHS-funded programs. |
| `NEWS-2026-001-C3` | Reasonable inference | The announced priority could affect future grant, partnership, or other funding choices. The page does not identify a particular affected organization or transaction. |

- **Allegation:** None contained in this record against a named outside organization.
- **Counterevidence / narrowing record:** The page supplies no implementing criteria, recusal record, funding notice, award change, termination, or measured result.
- **Missing link:** A dated decision record showing that the priority was applied to a specific organization, plus the responsible decision-maker, criteria, and resulting funding action.
- **Dependence cluster:** `HHS-PRIORITIES-2026-09-01`.
- **Update state:** New.
- **Functional comparison:** `Nomos` — the institution announces a rule for judging eligibility and integrity; `Plutus` — the rule is linked expressly to allocation of public funding. This is a system-function comparison, not an identification of Kennedy with either figure.
- **Alternative read:** The page may be an agenda statement rather than an independently enforceable standard.
- **Fiction bridge:** `CMP` — a treasury-temple announces that tainted patrons will lose access to the public well, while leaving “taint” undefined; the dramatic pressure comes from who gets to interpret the rule.

### NEWS-2026-002 — Proposed Pinnacle algorithmic-pricing consent decree

- **Actor / institution:** U.S. Department of Justice Antitrust Division; Office of the Associate Attorney General; Pinnacle Property Management Services LLC.
- **Event and publication date:** September 4, 2026.
- **Primary source:** [DOJ proposed Pinnacle consent decree announcement](https://www.justice.gov/opa/pr/justice-department-reaches-proposed-consent-decree-pinnacle-one-americas-largest-landlords)
- **Raw receipt:** DOJ press release 26-1026 and linked proposed judgment materials; accessed September 7, 2026.
- **Lifecycle:** `DET` allegations originated in the January 7, 2025 complaint; `DEC` proposed settlement filed; `ACT` restrictions would operate only if entered by the court; `EFF` pending public comment and judicial public-interest review.

| Claim ID | Status | Atomic proposition |
|---|---|---|
| `NEWS-2026-002-C1` | Established public-record fact | DOJ filed a proposed consent decree intended to resolve the United States' claims against Pinnacle in the RealPage rental-market enforcement action. |
| `NEWS-2026-002-C2` | Allegation | The United States alleges that Pinnacle participated with other landlords in using competitors' competitively sensitive information and pricing algorithms to coordinate rents. |
| `NEWS-2026-002-C3` | Established public-record fact | If approved, the proposed decree would restrict specified algorithmic pricing practices and competitor-data sharing, permit a monitor in stated circumstances, restrict participation in certain competitor meetings, and require cooperation with remaining claims. |
| `NEWS-2026-002-C4` | Reasonable inference | The matter tests whether a formally technical pricing process can function as coordinated allocation rather than independent market choice. |

- **Counterevidence / procedural limitation:** The decree is proposed, the underlying coordination statement remains an allegation, and the court has not yet entered final judgment.
- **Missing link:** Evidence that Attorney General Todd Blanche personally directed, approved, influenced, or recused from this matter. The release attributes the action to the Antitrust Division and Office of the Associate Attorney General, not to Blanche personally.
- **Dependence cluster:** `REALPAGE-PINNACLE-ANTITRUST`.
- **Update state:** New.
- **Functional comparison:** `Nomos` — enforcement defines the boundary between independent pricing and prohibited coordination; `Plutus` — the alleged mechanism concerns the distribution and extraction of housing payments; `Dolos` — available only as an allegation-level comparison if evidence establishes that the process was knowingly designed to conceal coordination or induce false reliance. Complexity or algorithm use alone is insufficient.
- **Alternative read:** Shared software or parallel pricing does not by itself prove an agreement; the government's pleaded and settlement records must carry that burden.
- **Fiction bridge:** `SYN` — rival landlords consult an oracle that claims merely to predict the market but may also make its own prophecy come true. The fictional oracle can be deceptive; the real-world record cannot be described that way without proof of design and intent.

## Story-seed boundary

The two cards can intersect fictionally without being merged factually:

```text
Nomos writes the eligibility rule.
Plutus controls the well and the rent gate.
The oracle calculates what everyone “independently” owes.
Dolos enters only if concealment or induced reliance is proved—or is clearly invented for the story.
```

No current record establishes coordination between HHS, the Pinnacle matter, Kennedy, or Blanche. Their conjunction exists only at the functional-comparison and fictional layers.

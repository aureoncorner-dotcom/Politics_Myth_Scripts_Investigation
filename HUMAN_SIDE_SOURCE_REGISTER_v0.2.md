# Human-Side Source Register and Adjudicated Claim Ledger v0.2

**Record cutoff:** 17 August 2026  
**Registry rebuilt:** 17 August 2026  
**Status:** Source-bearing revision-control authority for the integrated paper  
**Companion:** `HUMAN_SIDE_INSTITUTIONAL_PAPER_v1.0.md`

## 1. Controlling posture

This register implements the following order of authority:

1. A primary instrument controls the factual component it actually proves.
2. Independently verified secondary reporting may support a component when the primary instrument is unavailable, but it does not become primary merely because it quotes or links one.
3. `HUMAN_SIDE_RED_MARKER_RECONCILED_v0.2.md` controls later documentary corrections.
4. `HUMAN_SIDE_CANONICAL_HANDOFF_v0.1.md` supplies the prior claim-state and continuing do-not-state, null-result, counterevidence, and retired-arrow boundaries.
5. The raw investigation PDF is provenance-recovery material only. `The_Architecture_of_Capture.md (1)` is method/theory only. Neither is external-world evidence.
6. Model agreement, repetition, chronology alone, proximity, and symbolic material provide no evidentiary upgrade.

The supplied source-register skeleton contained sixty claim rows but no completed source objects. Its `P1`–`P6`, `X`, and `SRC-*` labels were classes, not citations. This version therefore preserves every inherited row while placing unsupported components on **HOLD** instead of filling them.

### Required dimensions

- **Finding type:** `FACT`, `ARCHITECTURE`, `LEGAL ELEMENT`, `CAUSAL JOIN`, or `INTENT/CONSIDERATION`.
- **Evidence state:** `ESTABLISHED`, `PROVISIONALLY ESTABLISHED`, `CONTESTED`, `OPEN`, `NOT ESTABLISHED`, `INDETERMINATE`, or `RETIRED/CORRECTED`.
- **Action:** `ADVANCE`, `HOLD`, `CLOSE ON CURRENT RECORD`, or `WRONG INSTRUMENT`.
- **Instrument class:** `P1` primary instrument; `P2` official record or formal party filing; `P3` verified secondary reporting; `P4` authenticated leak; `P5` interested-party analysis/allegation; `P6` contested empirical claim; `X` inference or bounded search result.
- **Provenance class:** `SRC-P` primary; `SRC-V` verified secondary; `SRC-L` leak-derived; `SRC-A` interested party; `SRC-U` unresolved.

### Source-object completeness

Every catalogued item has a live locator and retrieval date. No local evidentiary snapshot or cryptographic hash was created in this pass; each row is marked `LIVE LOCATOR — SNAPSHOT NOT CAPTURED`. That is an explicit preservation gap, not a blank field. Pinpoints are included where the recovered record made them available.

## 2. Source catalog

### 2.1 Legal and ethics framework

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-LAW-001` | `FAM-LAW-208` | U.S. House, Office of the Law Revision Counsel, **18 U.S.C. § 208** (current text retrieved 17 Aug. 2026) | P1 / SRC-P | https://uscode.house.gov/view.xhtml?req=%28title%3A18+section%3A208+edition%3Aprelim%29 | Elements and waiver route of §208; does not decide whether any investigated act was a covered particular matter or had a direct and predictable effect. |
| `SRC-LAW-002` | `FAM-LAW-208` | U.S. Office of Government Ethics, **5 C.F.R. Part 2640: Interpretation, Exemptions, Waiver Guidance Concerning 18 U.S.C. § 208** (retrieved 17 Aug. 2026) | P1 / SRC-P | https://www.oge.gov/web/oge.nsf/Resources/5%2BC.F.R.%2BPart%2B2640%3A%2BInterpretation%2C%2BExemptions%2BWaiver%2BGuidance%2BConcerning%2B18%2BU.S.C.%2B208%2B%28Acts%2BAffecting%2Ba%2BPersonal%2BFinancial%2BInterest%29 | General-applicability, exemption, and waiver framework; a regulatory exemption may leave no individualized waiver to find. |
| `SRC-LAW-003` | `FAM-OGE-CD` | U.S. Office of Government Ethics, **Certificates of Divestiture** training/guidance (retrieved 17 Aug. 2026) | P1 / SRC-P | https://extapps2.oge.gov/Training/OGETraining.nsf/0/FFB38ABC6D2E9F9885258AAF0055EE44 | Explains certificate process; does not establish that Blanche, Patel, or any other official received one. |
| `SRC-LAW-004` | `FAM-CIO-STATUTE` | U.S. Code, **44 U.S.C. § 3602** (current text retrieved 17 Aug. 2026) | P1 / SRC-P | https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title44-section3602 | Federal CIO appointment structure; helps identify the correct ethics-record route for a non-PAS appointment. |
| `SRC-LAW-005` | `FAM-OGE-DISCLOSURE` | U.S. Office of Government Ethics, **Public Financial Disclosure FAQs** (retrieved 17 Aug. 2026) | P1 / SRC-P | https://www.oge.gov/web/OGE.nsf/publicresources_disclosure-faq | Explains disclosure/ethics-agreement categories; does not prove which agency-held records exist for Barbaccia. |
| `SRC-LAW-006` | `FAM-JUDICIAL-RECUSAL` | U.S. Code, **28 U.S.C. § 455** (current text retrieved 17 Aug. 2026) | P1 / SRC-P | https://uscode.house.gov/view.xhtml?req=%28title%3A28%20section%3A455%20edition%3Aprelim%29 | General federal disqualification standard. It does not adjudicate a justice-specific fact pattern or establish what a justice knew. |

All catalog rows below were accessed on **17 August 2026** and have archive status **LIVE LOCATOR — SNAPSHOT NOT CAPTURED**, unless a later row says otherwise.

### 2.2 Religious-policy routing

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-RP-001` | `FAM-WH-FAITH` | White House, **Executive Order 14205, “Establishment of The White House Faith Office,”** 7 Feb. 2025 | P1 / SRC-P | https://www.whitehouse.gov/presidential-actions/2025/02/establishment-of-the-white-house-faith-office/ | Faith Office placement in the Domestic Policy Council; leadership and authorized coordinating, consultation, grant, business, agency-liaison, and AG-facing functions. Establishes authority, not improper preference. |
| `SRC-RP-002` | `FAM-WH-FAITH` | White House, **Executive Order 14202, “Eradicating Anti-Christian Bias,”** 6 Feb. 2025 | P1 / SRC-P | https://www.whitehouse.gov/presidential-actions/2025/02/eradicating-anti-christian-bias/ | DOJ task force, AG chair, broad membership, and recommendation route. Establishes public machinery, not misconduct. |
| `SRC-RP-003` | `FAM-DOJ-FAITH` | Department of Justice, **“Attorney General Pamela Bondi Hosts First Task Force Meeting to Eradicate Anti-Christian Bias,”** 22 Apr. 2025 | P2 / SRC-P | https://www.justice.gov/opa/pr/attorney-general-pamela-bondi-hosts-first-task-force-meeting-eradicate-anti-christian-bias | Official account of inaugural meeting and participating officials; proves attendance/agency account, not off-record coordination or the truth of every participant statement. |
| `SRC-RP-004` | `FAM-WH-FAITH` | White House, **Executive Order 14291, “Establishment of the Religious Liberty Commission,”** 1 May 2025 | P1 / SRC-P | https://www.whitehouse.gov/presidential-actions/2025/05/establishment-of-the-religious-liberty-commission/ | Commission, DOJ support, AG ex officio role, and advice to Faith Office/DPC. The order sunsets the Commission on 4 July 2026 unless extended; no extension instrument was recovered, so present-tense status after that date is HOLD. No improper-benefit finding. |
| `SRC-RP-005` | `FAM-DOJ-FAITH` | Department of Justice, **“Acting Attorney General Blanche Issues Updated Guidance to Strengthen Federal Religious Liberty,”** 23 July 2026 | P2 / SRC-P | https://www.justice.gov/opa/pr/acting-attorney-general-blanche-issues-updated-guidance-strengthen-federal-religious-liberty | Government-wide implementation domains: programs, employment, contracting, rulemaking, and enforcement. Official characterization; not proof of unconstitutional application. |
| `SRC-RP-006` | `FAM-DOJ-FAITH` | Department of Justice, **2026 Task Force Report: Eradicating Anti-Christian Bias Within the Federal Government**, Apr. 2026 | P2 / SRC-P | https://www.justice.gov/d9/2026-04/2026-task-force-report-eradicating-anti-christian-bias-within-the-federal-government-508_0.pdf | Task-force output and agency findings as government positions; does not independently prove the report's contested claims about prior conduct. |

### 2.3 Todd Blanche / DOJ / cryptocurrency

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-CR-001` | `FAM-OGE-BLANCHE` | U.S. Office of Government Ethics, **Todd Blanche Public Financial Disclosure (OGE 278)**, filed 2025 | P1 / SRC-P | https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index/4B1E6A519F015E7D85258C30003200C5/$FILE/Blanche%2C%20Todd%20%20final278.pdf | Entry holdings and value brackets. Use the filing's categories; “substantial” is descriptive, not an additional legal finding. |
| `SRC-CR-002` | `FAM-OGE-BLANCHE` | U.S. Office of Government Ethics, **Todd Blanche Ethics Agreement**, 10 Feb. 2025 | P1 / SRC-P | https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index/0E4C3EB0ACE8404785258C30003217F2/$FILE/Blanche%2C%20Todd%20%20finalEA.pdf | Divestiture/recusal commitments, including virtual-currency provisions; pp. 1–3 are load-bearing. Does not establish violation or identify a later case-specific authorization route. |
| `SRC-CR-003` | `FAM-DOJ-CRYPTO` | Department of Justice, **Memorandum, “Ending Regulation By Prosecution,”** 7 Apr. 2025 | P1 / SRC-P | https://www.justice.gov/dag/media/1395781/dl | Blanche's dated policy act; disbanding NCET and narrowing platform/registration-focused enforcement while retaining fraud, theft, terrorism, narcotics, trafficking, and other crime priorities. |
| `SRC-CR-004` | `FAM-OGE-BLANCHE` | U.S. Office of Government Ethics, **Todd Blanche Periodic Transaction Report (OGE 278-T)**, signed 3 June 2025 | P1 / SRC-P | https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index/9E22E6BED062C62D85258CC5002C7DEA/$FILE/Todd-Blanche-06.03.2025-278T.pdf | Late-May/2 June sales and report note concerning gifts of some crypto assets to adult children/grandchild. Establishes reported transactions, not their legal effect or completeness. |
| `SRC-CR-005` | `FAM-PRO-BLANCHE` | ProPublica, **“Top DOJ Official Shut Down Enforcement Against Crypto Companies While Holding Crypto Assets,”** 22 Dec. 2025 | P3 / SRC-V | https://www.propublica.org/article/todd-blanche-crypto-doj-trump | Independent reconstruction and DOJ's reported assertion that the issue was flagged, addressed, and cleared in advance. Establishes the existence/content of the attributed assertion, not its unseen reasoning. |
| `SRC-CR-006` | `FAM-SENATE-BLANCHE` | Six U.S. senators, **Letter to the Deputy Attorney General Regarding Cryptocurrency Conflicts**, 28 Jan. 2026 | P5 / SRC-A | https://www.hirono.senate.gov/imo/media/doc/20260128ltrfromsenatorstodagrecryptocurrencyconflicts.pdf | Formal oversight questions and requested instruments. Allegations/questions are not adjudicated facts. |
| `SRC-CR-007` | `FAM-SENATE-BLANCHE` | Senate Judiciary Committee Democrats, **Outstanding DOJ Oversight Requests**, 1 July 2026 | P2 for request status / SRC-A for accusations | https://www.judiciary.senate.gov/press/dem/releases/senate-judiciary-democrats-demand-todd-blanche-answer-to-dozens-of-oversight-requests-ignored-by-justice-department | Committee's stated response status. `NO RESPONSE` or `INSUFFICIENT RESPONSE` is not `DOCUMENT DOES NOT EXIST`. |
| `SRC-CR-008` | `FAM-CLC-BLANCHE` | Campaign Legal Center, **Complaint to DOJ Inspector General Regarding Deputy AG Todd Blanche**, 2026 | P5 / SRC-A | https://campaignlegal.org/document/clc-complaint-doj-inspector-general-regarding-deputy-ag-todd-blanche | Interested-party legal allegation and acquisition lead; not a legal finding or OIG disposition. |

### 2.4 Trump / World Liberty / crypto junction

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-TC-001` | `FAM-OGE-TRUMP-2026` | U.S. Office of Government Ethics, **Donald J. Trump 2026 Annual Public Financial Disclosure**, certified/released 30 June 2026 | P1 / SRC-P | https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index/69AEAA9D7455ACD585258E27002DDEE1/$FILE/Donald-J-Trump-2026-278ANNUAL.pdf | Filing components underlying income estimates. Requires direct page-by-page taxonomy before a project aggregate is stated. |
| `SRC-TC-002` | `FAM-OGE-TRUMP-2026` | Reuters, **“Trump reports more than $1.4 billion in income from crypto ventures,”** 30 June 2026 | P3 / SRC-V | https://www.reuters.com/world/us/trump-reports-more-than-14-billion-income-crypto-ventures-2026-06-30/ | Reuters's aggregate under its classification choices; not the project's number and not independent of the OGE filing for underlying amounts. |
| `SRC-TC-003` | `FAM-OGE-TRUMP-2026` | Associated Press, **Trump financial-disclosure analysis**, 30 June 2026 | P3 / SRC-V | https://apnews.com/article/trump-financial-disclosure-crypto-060c15062b8fedc6104159ea13775463 | AP's approximately/nearly $1.2B aggregate under a different denominator; not a second independent measurement of filing components. |
| `SRC-TC-004` | `FAM-WH-CRYPTO-POLICY` | White House, **Executive Order, “Strengthening American Leadership in Digital Financial Technology,”** 23 Jan. 2025 | P1 / SRC-P | https://www.whitehouse.gov/presidential-actions/2025/01/strengthening-american-leadership-in-digital-financial-technology/ | Administration digital-asset policy. Coexistence with family ventures is a structural junction, not motive or corruption. |
| `SRC-TC-005` | `FAM-WH-CRYPTO-POLICY` | White House, **Executive Order, “Establishment of the Strategic Bitcoin Reserve and United States Digital Asset Stockpile,”** 6 Mar. 2025 | P1 / SRC-P | https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/ | A second official policy instrument; does not by itself confer a particular private benefit. |
| `SRC-TC-006` | `FAM-MGX-BINANCE` | MGX/Binance, **“MGX Backs Binance in Landmark Investment,”** 12 Mar. 2025 | P2 issuer announcement / SRC-P for announcement | https://www.prnewswire.com/news-releases/mgx-backs-binance-in-landmark-investment-302400050.html | $2B investment announcement; interested transaction-party source and does not by itself establish later USD1 settlement details. |
| `SRC-TC-007` | `FAM-MGX-BINANCE` | The Guardian, **“Abu Dhabi firm to use Trump-linked stablecoin for $2bn Binance investment,”** 2 May 2025 | P3 / SRC-V | https://www.theguardian.com/us-news/2025/may/02/abu-dhabi-firm-binance-trump-stablecoin | Reported USD1 role and chronology. Does not establish consideration for clemency. |
| `SRC-TC-008` | `FAM-ZHAO-PARDON` | Associated Press, **Report on presidential pardon of Changpeng Zhao**, 23 Oct. 2025 | P3 / SRC-V | https://apnews.com/article/e1cb3fe516bc42b4c7ce5c107a280dc7 | Pardon event and surrounding chronology; explicitly insufficient for deal-to-pardon causation. |
| `SRC-TC-009` | `FAM-SENATE-ZHAO` | U.S. senators, **Oversight Letter Regarding Binance Pardon**, 2025 | P5 / SRC-A | https://www.banking.senate.gov/imo/media/doc/binancepardonletter.pdf | Questions and allegations; not proof of a quid pro quo. |

### 2.5 Palantir / state-data architecture

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-PL-001` | `FAM-DOD-MAVEN` | Department of Defense, **Contracts for May 21, 2025** | P1 / SRC-P | https://www.defense.gov/News/Contracts/Contract/Article/4194643/ | Palantir USG modification P00005 to W911QX-24-D-0012, $795M for Maven Smart System licenses, awarded 20 May. Does not establish later obligations beyond the modification or personal action by a named official. |
| `SRC-PL-002` | `FAM-ARMY-ESA` | U.S. Army, **“U.S. Army awards Enterprise Service Agreement to enhance military readiness and drive operational efficiency,”** 31 July 2025 | P2 / SRC-P | https://www.army.mil/article-amp/287506/u_s_army_awards_enterprise_service_agreement_to_enhance_military_readiness_and_drive_operational_efficiency | Consolidation of 75 contracts; up to ten years; $10B maximum potential. The Army expressly says the ceiling is not a specific obligation or commitment. |
| `SRC-PL-003` | `FAM-ICE-70CTD` | USAspending, **Award 70CTD022FR0000170** (live award record) | P1 / SRC-P | https://www.usaspending.gov/award/CONT_AWD_70CTD022FR0000170_7012_GS35F0086U_4730 | Award/action history and recipient. Does not prove use, accuracy, outcome, steering, or individual approval. |
| `SRC-PL-004` | `FAM-ICE-70CTD` | ICE, **Limited-Sources Justification for 70CTD022FR0000170**, 17 Apr. 2025 (document mirror) | P1 / SRC-P | https://iptp-production.s3.amazonaws.com/media/documents/2025.04.17_ICE_Limited_Sources_Justification_for_70CTD022FR0000170.pdf | ICE's stated urgency/need and procurement route. Agency rationale is not an independent proof that dependency was unavoidable. Original 2022 route remains to be reconciled. |
| `SRC-PL-005` | `FAM-ICE-70CTD` | SAM.gov, **Sole-source notice ICE_JA-25-0266**, 16 Jan. 2026 | P1 / SRC-P | https://sam.gov/opp/5477991867424397affe85e2fad8b5fc/view | Later sole-source notice. Exact IP/system/migration language requires the attached justification. |
| `SRC-PL-020` | `FAM-ICE-70CTD` | SAM.gov, **Original 2022 notice for the Palantir ICE order** | P1 / SRC-P | https://sam.gov/opp/027b10d0cff3409c91d52d5cef37d576/view | Page labels authority “Only One Source (except brand name).” It must be reconciled with FPDS-derived competition/fair-opportunity fields and later logical-follow-on language. |
| `SRC-PL-021` | `FAM-ICE-70CTD` | FPDS.gov, **ICE/Palantir award-action query, 70CTD022FR0000170** | P1 / SRC-P | https://www.fpds.gov/ezsearch/fpdsportal?indexName=awardfull&length=50&q=palantir+VENDOR_FULL_NAME%3A%22PALANTIR+TECHNOLOGIES+INCORPORATED%22+DEPARTMENT_FULL_NAME%3A%22HOMELAND+SECURITY%2C+DEPARTMENT+OF%22+CONTRACTING_AGENCY_NAME%3A%22U.S.+IMMIGRATION+AND+CUSTOMS+ENFORCEMENT%22&renderer=jsp&s=FPDS.GOV&templateName=PDF | FPDS-derived action and competition fields. Coding does not resolve the underlying source-selection route without the complete award/J&A. |
| `SRC-PL-006` | `FAM-CMS-IEA` | Centers for Medicare & Medicaid Services, **CMS Information Exchange Agreement (IEA)** (policy page) | P1 / SRC-P | https://security.cms.gov/learn/cms-information-exchange-agreement-iea | General formal-instrument requirements for protected interagency data exchange. Does not prove a particular agreement existed or was breached. |
| `SRC-PL-007` | `FAM-CA-HHS-DOCKET` | California Attorney General, **Medicaid-data preliminary-relief announcement**, 12 Aug. 2025 | P2 / SRC-P | https://oag.ca.gov/news/press-releases/attorney-general-bonta-secures-preliminary-relief-blocking-california%E2%80%99s-medicaid | Litigation baseline and claimed scope; press release is not the order itself. |
| `SRC-PL-008` | `FAM-CA-HHS-DOCKET` | U.S. District Court, N.D. Cal., **Order Granting in Part and Denying in Part Preliminary Injunction, California v. HHS, No. 3:25-cv-05536, Dkt. 98**, 12 Aug. 2025 | P1 / SRC-P | https://oag.ca.gov/system/files/attachments/press-docs/98%20Order%20Granting%20in%20Part%20and%20Denying%20in%20Part%20PI.pdf | Court's actual preliminary-relief terms and findings at that stage; not a final merits judgment. |
| `SRC-PL-009` | `FAM-CA-HHS-DOCKET` | California plaintiffs, **Motion to Enforce Preliminary Injunction, Dkt. 151**, filed 26 Mar. 2026 | P2 party filing / SRC-P for filing | https://oag.ca.gov/system/files/attachments/press-docs/151%20Pls%20Mot%20to%20Enforce.pdf | Pp. 2–5 quote government representations: ICE held a large/complex dataset, no ingestion into officer systems/no law-enforcement use as of stated dates, quarantine, filtering claims. Pp. 6–9 are plaintiffs' argument, not findings. |
| `SRC-PL-010` | `FAM-CA-HHS-DOCKET` | CourtListener, **Rich declaration, Dkt. 182-1**, July 2026 | P2 / SRC-P, located not fully ingested | https://www.courtlistener.com/docket/70687026/182/1/state-of-california-v-us-department-of-health-and-human-services/ | Underlying primary acquisition target for custody/deletion evidence. `LOCATED — DIRECT ATTACHMENT REVIEW STILL REQUIRED`; not used alone to carry prose. |
| `SRC-PL-011` | `FAM-CA-HHS-DOCKET` | CourtListener, **Exhibit/transcript, Dkt. 182-2**, July 2026 | P2 / SRC-P, located not fully ingested | https://www.courtlistener.com/docket/70687026/182/2/state-of-california-v-us-department-of-health-and-human-services/ | Same docket family and review limitation as `SRC-PL-010`; not independent corroboration. |
| `SRC-PL-012` | `FAM-CA-HHS-DOCKET` | NPR/KCLU, **“ICE shared Medicaid data it wasn't supposed to have with Palantir,”** 17 July 2026 | P3 / SRC-V | https://www.kclu.org/science-technology/2026-07-17/ice-shared-medicaid-data-it-wasnt-supposed-to-have-with-palantir?_amp=true | Reports Teams transfer to Palantir personnel, deletion request, later copies, and counterstatements that ICE did not use it for law enforcement and Palantir purged it. Does not prove ELITE ingestion or person-level consequences. |
| `SRC-PL-013` | `FAM-GSA-BARBACCIA` | General Services Administration, **“Greg Barbaccia Appointed Acting Director of the Technology Transformation Services,”** 19 Feb. 2026 | P2 / SRC-P | https://www.gsa.gov/about-gsa/newsroom/news-releases/greg-barbaccia-appointed-acting-director-of-the-tts-02192026 | Appointment effective 19 Feb. 2026. A 7 May page-update date is not the appointment date. |
| `SRC-PL-014` | `FAM-BARBACCIA-RETURN` | Nextgov/FCW, **“Greg Barbaccia to leave federal CIO role at end of August,”** July 2026 | P3 / SRC-V | https://www.nextgov.com/people/2026/07/greg-barbaccia-leave-federal-cio-role-end-august/414620/ | Reported departure date; future-state reporting at cutoff. |
| `SRC-PL-015` | `FAM-BARBACCIA-RETURN` | Nextgov/FCW, **“Greg Barbaccia to return to Palantir after leaving government,”** 31 July 2026 | P3 / SRC-V | https://www.nextgov.com/people/2026/07/greg-barbaccia-return-palantir-after-leaving-government/415149/ | Reported future return after 31 Aug.; no completed return, exact role, or start date at cutoff. |
| `SRC-PL-016` | `FAM-OGE-BARBACCIA` | ProPublica, **Gregory J. Barbaccia disclosure compilation** | P3 secondary extraction / SRC-V | https://projects.propublica.org/trump-team-financial-disclosures/appointees/barbaccia-gregory-j/ | Entry PLTR bracket reportedly $1,001–$15,000. Does not show retention, disposition, waiver, recusal, or participation. |
| `SRC-PL-017` | `FAM-OGE-PATEL` | U.S. Office of Government Ethics, **Kashyap Patel Ethics Agreement**, 28 Jan. 2025 | P1 / SRC-P | https://extapps2.oge.gov/201/Presiden.nsf/PAS%2BIndex/730D7A12BBF6654785258C240032196E/%24FILE/Patel%2C%20Kashyap%20%20finalEA.pdf | Pp. 4–5 require PLTR divestiture within 90 days and interim recusal. Does not establish participation or nonparticipation in a particular procurement. |
| `SRC-PL-018` | `FAM-OGE-PATEL` | U.S. Office of Government Ethics, **Kashyap Patel Periodic Transaction Report**, filed 21 July 2025 | P1 / SRC-P | https://static.notus.org/3b/61/46d6712d4aff9412d01276fbf797/kashyap-patel-07-21-2025-278t.pdf | Reports PLTR sale on 12 May 2025 in $50,001–$100,000 bracket. Required mitigation is neither guilt nor exoneration. |
| `SRC-PL-019` | `FAM-HHS-MINOR` | ProPublica, **Clark Minor disclosure compilation** | P3 secondary extraction / SRC-V | https://projects.propublica.org/trump-team-financial-disclosures/appointees/minor-clark/ | Reports prior Palantir role, PLTR bracket, and 9 July 2025 sale. Not authority to add a new claim or infer approval of data sharing. Held as a lead only. |

### 2.6 Access, amplification, and Dialog

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-PA-001` | `FAM-BANNON-SPEAKER` | Washington Post, **“How Mike Johnson clinched the speakership — with an assist from Trump,”** 3 Jan. 2025 | P3 / SRC-V | https://www.washingtonpost.com/politics/2025/01/03/johnson-speaker-vote-trump/ | Reports that Bannon used *War Room* to urge members to support Johnson during the Speaker vote. Does not isolate Bannon's causal effect; Trump calls and Johnson's promises are alternative mechanisms. |
| `SRC-PA-002` | `FAM-JOHNSON-BERGER` | ProPublica, **“Mike Johnson Is Living With an Evangelical Influence Seeker,”** 27 Feb. 2025 | P3 / SRC-V | https://www.propublica.org/article/mike-johnson-evangelical-pastor-steve-berger-roommates | Reported co-residence/access setting and outside advocacy. Preserves Johnson spokesperson's statements: fair-market rent and no policy discussions with Berger. Does not prove Berger-caused action. |
| `SRC-PA-003` | `FAM-JOHNSON-BERGER` | Semafor, **“House Speaker Mike Johnson rents house from colleague,”** 30 Apr. 2025 | P3 / SRC-V | https://www.semafor.com/article/04/30/2025/house-speaker-mike-johnson-rents-house-from-colleague | Reports relocation roughly one month after prior story and new Issa rental. Establishes an endpoint to the reported co-residence, not motive. |
| `SRC-PA-004` | `FAM-DIALOG-LEAK-2026` | WIRED, **“Leak Exposes Members of Peter Thiel's Secretive ‘Dialog’ Society,”** 16 June 2026, with correction | P4 / SRC-L | https://www.wired.com/story/leak-exposes-members-of-peter-thiels-secretive-dialog-society/ | Verified leak-based registration/access reporting and scheduled 2026 retreat. Correction concerns a Jeff Epstein identity conflation; it is not a wholesale retraction. Registration is not attendance or agreement. |
| `SRC-PA-005` | `FAM-DIALOG-FOUNDING` | Axios, **Report on Dialog's private network and founders**, 7 Aug. 2025 | P3 / SRC-V | https://www.axios.com/2025/08/07/dialog-secret-network-thiel-hoffman | Independent support for Dialog's existence/founding and private-access structure; not independent corroboration of the 2026 leaked roster. |
| `SRC-PA-006` | `FAM-PALANTIR-ISSUER` | Palantir Technologies, **Board of Directors** (retrieved 17 Aug. 2026) | P2 issuer record / SRC-P for issuer fact | https://investors.palantir.com/board.html | Thiel's Palantir co-founder/chairman role. Combined with `SRC-PA-004/005`, establishes only a common-founder overlap, not influence, command, or procurement. |
| `SRC-PA-007` | `FAM-DIALOG-CANCEL` | RTÉ News, **“Dialog group event at Powerscourt in Wicklow cancelled,”** 3 July 2026 | P3 / SRC-V | https://www.rte.ie/news/2026/0703/1581622-powerscourt-dialog/ | Event cancellation before 12–16 Aug. dates. Retires actual 2026 co-attendance at that event. |
| `SRC-PA-008` | `FAM-AI-MORATORIUM` | Congress.gov, **S.Amdt. 2814 to H.R. 1**, 1 July 2025 | P1 / SRC-P | https://www.congress.gov/amendment/119th-congress/senate-amendment/2814/all-info | Primary legislative record for removal of the proposed state-AI-law moratorium; no evidence of which outside advocate caused the action. |
| `SRC-PA-009` | `FAM-AI-MORATORIUM` | U.S. Senate, **Roll Call Vote 363, 119th Congress, 1st Session**, 1 July 2025 | P1 / SRC-P | https://www.senate.gov/legislative/LIS/roll_call_votes/vote1191/vote_119_1_00363.htm | Records the 99–1 vote; outcome only, not causal attribution. |
| `SRC-PA-010` | `FAM-AI-MORATORIUM-REPORTING` | The Verge, **Report on Ted Cruz, Steve Bannon, and the AI-moratorium fight**, 11 July 2025 | P3 / SRC-V | https://www.theverge.com/politics/704424/ai-moratorium-ted-cruz-steve-bannon-trump | Supports Bannon's public pressure/amplification role. Does not isolate his effect or prove a private command channel. |
| `SRC-PA-011` | `FAM-AI-MORATORIUM-REPORTING` | Associated Press, **Report on Republican opposition and removal of the AI moratorium**, 3 July 2025 | P3 / SRC-V | https://apnews.com/article/artificial-intelligence-republicans-trump-tax-bill-97d700da09cac62aa510eb4411bab24e | Documents a broad opposition coalition. This is counterevidence to causal primacy by any one amplifier. |

### 2.7 Judiciary and confirmation architecture

| Source ID | Family | Issuer, title, date | Class | Durable locator | Supports; limits |
|---|---|---|---|---|---|
| `SRC-JU-001` | `FAM-FEDSOC-LEO` | Federalist Society, **Leonard A. Leo biography** (retrieved 17 Aug. 2026) | P2 self-description / SRC-P for statement | https://fedsoc.org/ttd-topics/leonard-leo | Leo's stated Trump judicial-selection and Gorsuch/Kavanaugh selection/confirmation role, and earlier outside-coalition work. Self-description does not prove continuing control after appointment. |
| `SRC-JU-002` | `FAM-SENATE-SCOTUS` | U.S. Senate, **Supreme Court Nominations, 1789–Present** | P1 / SRC-P | https://www.senate.gov/legislative/nominations/SupremeCourtNominations1789present.htm | Nomination, action, and vote chronology. Does not establish improper motive. |
| `SRC-JU-003` | `FAM-SENATE-SCOTUS` | U.S. Senate, **About Judicial Nominations — Historical Overview** | P1 / SRC-P | https://www.senate.gov/about/powers-procedures/nominations/judicial-nominations-overview.htm | Senate role; no action on Garland; rule change and later confirmations. Gatekeeping is constitutional authority, not itself misconduct. |
| `SRC-JU-004` | `FAM-MCCONNELL-GARLAND` | Senate Republican Leader, **“McConnell on Supreme Court Nomination,”** 16 Mar. 2016 | P2 / SRC-P | https://www.republicanleader.senate.gov/newsroom/remarks/mcconnell-on-supreme-court-nomination | McConnell's contemporaneous position that the Senate would not proceed. Proves announced gatekeeping decision, not a legal violation. |
| `SRC-JU-005` | `FAM-JCN-CAMPAIGNS` | Judicial Crisis Network, **“JCN Launches $10 Million Campaign … Support President-Elect Trump Nominee,”** 9 Jan. 2017 | P2 interested self-report / SRC-A | https://judicialnetwork.com/jcn-press-release/judicial-crisis-network-launches-10-million-campaign-preserve-justice-scalias-legacy-support-president-elect-trump-nominee/ | JCN's own announced $7M Garland effort and planned $10M confirmation campaign. Self-reported spending requires financial records for exact expenditure. |
| `SRC-JU-006` | `FAM-JCN-CAMPAIGNS` | Judicial Crisis Network, **“JCN Launches Multimillion-Dollar Initial Ad Blitz to Fill Supreme Court Seat,”** Sept. 2020 | P2 interested self-report / SRC-A | https://judicialnetwork.com/in-the-news/jcn-launches-multimillion-dollar-initial-ad-blitz-to-fill-scotus-seat/ | $2.2M initial Barrett-related phase and stated earlier campaigns. Not an audited total. |
| `SRC-JU-007` | `FAM-MARBLE-990` | IRS-derived Form 990 via ProPublica Nonprofit Explorer, **Marble Freedom Trust, FY ending Apr. 2021** | P1 filing data / SRC-P | https://projects.propublica.org/nonprofits/organizations/850784793 | $1,603,791,362 contributions, total revenue/assets, and officers from the filing. Does not identify Seid by itself or tie funds to earlier confirmations. |
| `SRC-JU-008` | `FAM-SEID-MARBLE` | ProPublica, **“How a Secretive Billionaire Handed His Fortune to the Architect of the Right-Wing Takeover of the Courts,”** 2022 | P3 / SRC-V | https://www.propublica.org/article/dark-money-leonard-leo-barre-seid | Source-bearing reconstruction of Seid → Tripp Lite → Marble transfer/sale. The 2020 formation/2021 sale chronology defeats a direct arrow to Gorsuch, Kavanaugh, or Barrett confirmation spending absent a separate earlier transfer. |
| `SRC-JU-009` | `FAM-LEO-NETWORK` | ProPublica, **“We Don't Talk About Leonard: The Man Behind the Right's Supreme Court Supermajority,”** 2023 | P3 / SRC-V | https://www.propublica.org/article/we-dont-talk-about-leonard-leo-supreme-court-supermajority | Broader network/funding reconstruction. Concentrated outlet family; does not establish post-confirmation command or a purchased judgment. |
| `SRC-JU-010` | `FAM-THOMAS-CROW` | ProPublica, **“Clarence Thomas Secretly Accepted Luxury Trips From GOP Donor Harlan Crow,”** 6 Apr. 2023 | P3 / SRC-V | https://www.propublica.org/article/clarence-thomas-scotus-undisclosed-luxury-travel-gifts-crow | Benefits/access and disclosure history as reported. No case-specific consideration or outcome join. |
| `SRC-JU-011` | `FAM-THOMAS-CROW` | ProPublica, **“Clarence Thomas Defends Undisclosed ‘Family Trips’ … Here Are the Facts,”** 7 Apr. 2023 | P3 / SRC-V | https://www.propublica.org/article/clarence-thomas-response-trips-legal-experts-harlan-crow | Thomas's counterposition and legal dispute. Same outlet/source family as `SRC-JU-010`, not independent corroboration. |
| `SRC-JU-012` | `FAM-THOMAS-CROW` | ProPublica, **“Clarence Thomas Acknowledges Undisclosed Real Estate Deal … and Discloses Private Jet Flights,”** 31 Aug. 2023 | P3 with linked filing / SRC-V | https://www.propublica.org/article/clarence-thomas-disclosure-filing-harlan-crow-real-estate-travel-scotus | Amendment/disclosure response. Establishes later reporting action, not purchased outcomes. |
| `SRC-JU-013` | `FAM-ALITO-SINGER` | ProPublica, **“Justice Samuel Alito Took Luxury Fishing Vacation With GOP Billionaire Who Later Had Cases Before the Court,”** 20 June 2023 | P3 / SRC-V | https://www.propublica.org/article/samuel-alito-luxury-fishing-trip-paul-singer-scotus-supreme-court | Travel/access and later case intersection; preserves Alito's contrary position. NML Capital's 7–1 result is counterevidence to a bespoke-vote claim. No purchased vote is established. |
| `SRC-JU-014` | `FAM-GORSUCH-DUFFY` | Washington Post, **“Gorsuch property sale renews calls for Supreme Court ethics reform,”** 25 Apr. 2023 | P3 / SRC-V | https://www.washingtonpost.com/politics/2023/04/25/neil-gorsuch-property-sale-law-firm-ethics/ | Sale, disclosure description, and later firm/court intersection. Preserves Duffy's statement that he had not met/spoken with Gorsuch and consulted firm ethics personnel. No favorable-treatment join. |
| `SRC-JU-015` | `FAM-JUD-DISCLOSURE` | Administrative Office of the U.S. Courts, **Judiciary Financial Disclosure Reports** | P1 / SRC-P | https://www.uscourts.gov/administration-policies/judiciary-financial-disclosure-reports | Primary acquisition portal. A portal is not a substitute for the individual report/pinpoint. |
| `SRC-JU-016` | `FAM-SCOTUS-CODE` | Supreme Court of the United States, **Code of Conduct for Justices of the Supreme Court**, 13 Nov. 2023 | P1 / SRC-P | https://www.supremecourt.gov/about/code-of-conduct-for-justices_november_13_2023.pdf | General ethics/recusal framework. Does not adjudicate a particular justice's conduct and postdates some events. |
| `SRC-JU-017` | `FAM-ROBERTS-SPOUSE` | Washington Post, **“Supreme Court Justices Thomas, Alito delay 2022 financial disclosures,”** 7 June 2023 | P3 / SRC-V | https://www.washingtonpost.com/politics/2023/06/07/supreme-court-justice-disclosures-clarence-thomas/ | Reports amended description of Jane Roberts's compensation and an accuser's concern. Does not supply the required commission → firm → case → Roberts participation chain. |
| `SRC-JU-018` | `FAM-THOMAS-DISCLOSURE` | Clarence Thomas, **2023 Annual Financial Disclosure (AO 10 mirror)**, filed 2024 | P1 / SRC-P | https://fixthecourt.com/wp-content/uploads/2024/06/Thomas-Clarence-Annual-2023.pdf | Justice-specific filing and amendments as reported on the form. Mirror locator should be replaced with the judiciary-hosted copy if acquired. |
| `SRC-JU-019` | `FAM-ALITO-NML` | Supreme Court of the United States, **Republic of Argentina v. NML Capital, Ltd., 573 U.S. 134 (2014)** | P1 / SRC-P | https://www.govinfo.gov/app/details/USREPORTS-573/USREPORTS-573-134/context | Opinion and 7–1 disposition. Relevant counterevidence to a bespoke-vote inference; does not resolve disclosure or recusal questions. |
| `SRC-JU-020` | `FAM-GORSUCH-DISCLOSURE` | Neil Gorsuch, **2017 Annual Financial Disclosure (AO 10 mirror)** | P1 / SRC-P | https://fixthecourt.com/wp-content/uploads/2018/06/Gorsuch-NM-J3.-SUP_R_17.pdf | Primary filing text as mirrored; supports what was disclosed, not the buyer's identity or a legal conclusion. |
| `SRC-JU-021` | `FAM-GORSUCH-DUFFY` | Politico, **Report on Gorsuch's Colorado property sale**, 25 Apr. 2023 | P3 / SRC-V | https://www.politico.com/news/2023/04/25/neil-gorsuch-colorado-property-sale-00093579 | Transaction reconstruction and Duffy's counterstatement; no influence or favorable-treatment finding. |
| `SRC-JU-022` | `FAM-ROBERTS-SPOUSE` | Kendal B. Price, **Sworn Affidavit**, 2 Dec. 2022 | P5 sworn allegation / SRC-A | https://www.documentcloud.org/documents/23791123-2-of-8-sworn-affidavit-of-kendal-b-price-12-02-2022 | Source-bearing allegation about recruiter compensation. Does not independently verify amounts or supply the firm/client/case/participation join. |
| `SRC-JU-023` | `FAM-JUDICIAL-ADVISORY` | Judicial Conference, **Advisory Opinion No. 107, Disqualification Based on Spouse's Business Relationships** | P1 / SRC-P | https://www.uscourts.gov/sites/default/files/vol02b-ch02_0.pdf | General counterweight rejecting automatic disqualification from every matter involving a spouse's business contacts; case-specific facts still govern. |

## 3. Adjudicated claim ledger

An external source ID supports only the component described in the catalog. `REQ-*` is a missing-instrument target, not evidence. `LOG-01` is the bounded source-recovery audit of the supplied corpus and public locators on 17 Aug. 2026; it proves only what this pass located or did not locate.

### Packet 1 — religious-policy routing

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `RP-01` | FACT | **ESTABLISHED — ADVANCE.** Faith Office is housed in DPC and has stated executive coordinating functions. | `SRC-RP-001` | Ordinary executive coordination is the null. |
| `RP-02` | FACT | **ESTABLISHED — ADVANCE.** White-Cain's role and Office authority to consult outside leaders and recommend policy are documented. | `SRC-RP-001` | Consultation is not improper influence; need outside actor → recommendation → action. |
| `RP-03` | FACT | **ESTABLISHED — ADVANCE.** Formal authority connects the Office to the AG and agency/grant coordination. | `SRC-RP-001` | Lawful religious-liberty enforcement/equal access remains the strongest ordinary explanation. |
| `RP-04` | FACT | **ESTABLISHED — ADVANCE.** DOJ chaired a broad interagency task force with named senior participants. | `SRC-RP-002`, `SRC-RP-003` | Membership/attendance is not secret coordination. |
| `RP-05` | ARCHITECTURE | **ESTABLISHED — ADVANCE TO CONSEQUENCE TEST.** Policy converted into guidance reaching programs, employment, contracting, rulemaking, and enforcement. | `SRC-RP-004`, `SRC-RP-005`, `SRC-RP-006` | Need a specific organization, pre-decision route, action, benefit/exclusion, and governing exception. The Commission's post-4 July 2026 status is HOLD absent an extension instrument. |
| `RP-06` | CAUSAL JOIN | **OPEN — HOLD.** Improper religious capture is not established. | `NO SUPPORTING SOURCE`; `REQ-RP-01` | Missing: privileged access → selective action/consequence; do not infer it from structure. |

### Packet 2 — Blanche / DOJ / cryptocurrency

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `CR-01` | FACT | **ESTABLISHED — ADVANCE.** Blanche entered office with disclosed crypto and crypto-related interests in filing-defined brackets. | `SRC-CR-001`, `SRC-CR-002` | Use verbatim asset/bracket taxonomy; no legal conclusion from value alone. |
| `CR-02` | LEGAL ELEMENT | **ESTABLISHED — ADVANCE.** Ethics agreement imposed divestiture and interim-recusal commitments. | `SRC-CR-002`, `SRC-LAW-001` | A restriction is not proof it was breached. |
| `CR-03` | FACT | **ESTABLISHED — ADVANCE.** 7 Apr. memo preceded reported late-May/2 June divestitures. | `SRC-CR-003`, `SRC-CR-004` | Chronology alone is not §208 liability or intent. |
| `CR-04` | FACT | **ESTABLISHED — ADVANCE.** Memo disbanded NCET and narrowed specified enforcement routes while retaining named crime priorities. | `SRC-CR-003` | Preserve retained priorities; do not say DOJ ended crypto enforcement. |
| `CR-05` | FACT | **ESTABLISHED — ADVANCE.** Relevant sales/transfers were reported after the memo. | `SRC-CR-004` | Adult-child gifts and any CD require separate legal/transaction analysis. |
| `CR-06` | FACT (attributed position) | **ESTABLISHED ONLY AS DOJ'S REPORTED POSITION — HOLD LEGAL CONCLUSION.** | `SRC-CR-005` | “Cleared in advance” does not reveal decisionmaker, route, scope, or reasoning. |
| `CR-07` | FACT (oversight status) | **ESTABLISHED ONLY AS COMMITTEE-REPORTED STATUS — HOLD INFERENCE.** | `SRC-CR-006`, `SRC-CR-007` | `NO RESPONSE` is not `NO CLEARANCE`; accusations remain interested assertions. |
| `CR-08` | LEGAL ELEMENT | **OPEN — HOLD.** §208 application and authorization path remain unresolved. | `SRC-LAW-001`, `SRC-LAW-002`, `SRC-CR-002`, `SRC-CR-003`, `SRC-CR-005`, `REQ-CR-01` | Determine covered particular matter/general applicability, direct/predictable effect, waiver, exemption, no-covered-matter analysis, and screening. |
| `CR-09` | INTENT/CONSIDERATION | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** No recovered evidence proves bribery, payment, coordinated trade, quid pro quo, or intentional self-enrichment. | `LOG-01`; reviewed `SRC-CR-001`–`008` | This is a bounded null result, not exoneration; reopen only on direct consideration/intent evidence. |

### Packet 2B — Trump / World Liberty / crypto

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `TC-01` | FACT / AGGREGATE | **INDETERMINATE — HOLD FOR DIRECT RECALCULATION.** The filing shows very large digital-asset-linked income, but published totals use incompatible denominators. | `SRC-TC-001`, `SRC-TC-002`, `SRC-TC-003`, `REQ-TC-01` | Do not adopt $580M, ~$1.2B, >$1.4B, or a range between them as the project's total. |
| `TC-02` | ARCHITECTURE | **ESTABLISHED AT STRUCTURAL-JUNCTION LEVEL — ADVANCE.** Official digital-asset policy coexisted with large family crypto income. | `SRC-TC-001`, `SRC-TC-004`, `SRC-TC-005` | Structural overlap is not motive; presidential legal analysis is not the Blanche/employee §208 analysis. |
| `TC-03` | FACT / CHRONOLOGY | **ESTABLISHED AS SEPARATE EVENTS — ADVANCE CAUTIOUSLY.** MGX/Binance transaction, reported USD1 settlement route, and later pardon are documented. | `SRC-TC-006`, `SRC-TC-007`, `SRC-TC-008` | The events' coexistence does not establish transaction → pardon. MGX and USD1 components come from different source types. |
| `TC-04` | CAUSAL JOIN / INTENT | **OPEN AND PRESENTLY UNSUPPORTED — HOLD.** | `SRC-TC-009` only as oversight allegation; `REQ-TC-02` | Need clemency recommendations, lobbying/contact records, communications, or consideration; do not state that WLF purchased a pardon. |

### Packet 3 — Palantir / state-data architecture

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `PL-01` | FACT | **ESTABLISHED WITH ENUMERATED SCOPE — ADVANCE.** Recovered instruments show Palantir in defense, Army, and ICE environments. | `SRC-PL-001`, `SRC-PL-002`, `SRC-PL-003` | Do not generalize beyond enumerated records; shared vendor is not shared command. |
| `PL-02` | FACT | **ESTABLISHED — ADVANCE.** P00005/W911QX-24-D-0012 was $795M for Maven licenses. | `SRC-PL-001` | Do not aggregate overlapping orders or equate award/modification value with final spend without records. |
| `PL-03` | FACT | **ESTABLISHED — ADVANCE.** Army agreement consolidated 75 contracts with a $10B maximum potential over up to ten years. | `SRC-PL-002` | The ceiling is not committed spend; preserve Army's efficiency rationale. |
| `PL-04` | ARCHITECTURE | **PROVISIONALLY ESTABLISHED — HOLD COMPARATIVE “LOCK-IN” CLAIM.** Limited/sole-source instruments evidence incumbency and dependency questions. | `SRC-PL-003`, `SRC-PL-004`, `SRC-PL-005`, `SRC-PL-020`, `SRC-PL-021`, `REQ-PL-01` | Reconcile 2022 one-source/fair-opportunity records; obtain full J&A, market research, alternatives, and base rate before “unusual lock-in.” |
| `PL-05` | LEGAL/PROCESS ELEMENT | **ESTABLISHED AS GENERAL POLICY ONLY — HOLD CASE-SPECIFIC COMPLIANCE CLAIM.** | `SRC-PL-006` | Policy does not prove an IEA existed, was required on exactly these facts, or was breached; obtain operative agreement(s). |
| `PL-06` | FACT | **ESTABLISHED AT NARROW CUSTODY-ROUTE LEVEL — ADVANCE TO EVENT TABLE.** CMS/HHS data reached ICE and was later shared with Palantir personnel. | `SRC-PL-007`, `SRC-PL-008`, `SRC-PL-009`, `SRC-PL-012`; `SRC-PL-010/011` located | Same docket family is one lineage. Attach/read Dkt. 182 exhibits before relying on residual-copy counts or exact transfer details. |
| `PL-07` | CAUSAL JOIN | **NOT ESTABLISHED — HOLD.** No recovered record ties the disputed dataset to ELITE ingestion, target generation, address, arrest, detention, or removal. | `SRC-PL-009`, `SRC-PL-012`, `REQ-PL-02` | Need system logs, queries, outputs, audit trails, discovery, or person-level enforcement records. |
| `PL-08` | ARCHITECTURE / LEGAL CHARACTERIZATION | **PROVISIONALLY ESTABLISHED; CHARACTERIZATION CONTESTED — ADVANCE CAUTIOUSLY.** Teams transfer/deletion/copy-control history supports a custody-control failure question. | `SRC-PL-008`, `SRC-PL-009`, `SRC-PL-012` | Preserve counterevidence: no ingestion/use representations and Palantir's purge statement. Do not collapse custody into harm. |
| `PL-09` | FACT / CHRONOLOGY | **ESTABLISHED AS REVOLVING-DOOR SEQUENCE THROUGH A REPORTED FUTURE PLAN — HOLD COMPLETION.** | `SRC-PL-013`, `SRC-PL-014`, `SRC-PL-015` | Appointment was 19 Feb. 2026; at cutoff, post-31 Aug. return was not completed and role/start were unclear. Recheck after 31 Aug. |
| `PL-10` | FACT / LEGAL ELEMENT | **OPEN — HOLD.** One secondary extraction shows an entry PLTR bracket but no disposition. | `SRC-PL-016`, `SRC-LAW-004`, `SRC-LAW-005`, `REQ-PL-03` | Do not state stock retention. Seek OMB/GSA 278e/278-Ts, recusal/screening/§208 advice, waivers if any. A PAS nominee ethics agreement may be the wrong instrument. |
| `PL-11` | CAUSAL JOIN / INTENT | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** No recovered source ties Barbaccia to Palantir-specific steering. | `LOG-01`, `SRC-PL-013`–`016`, `REQ-PL-03` | Reopen only with participation records, communications, procurement role, or consideration evidence. |
| `PL-12` | FACT | **ESTABLISHED — ADVANCE AS MITIGATION.** Patel's agreement required PLTR divestiture and the PTR reports a 12 May 2025 sale. | `SRC-PL-017`, `SRC-PL-018` | Required compliance is neither guilt nor exoneration. |
| `PL-13` | CAUSAL JOIN | **OPEN — HOLD.** No recovered record shows Patel's matter-specific participation affecting Palantir. | `SRC-PL-017`, `SRC-PL-018`, `REQ-PL-04` | Need agenda, approval, procurement, recusal, or communication records. |
| `PL-14` | CAUSAL JOIN | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** Multiple contracts/career links do not establish unified command. | `LOG-01`, `SRC-PL-001`–`019` | No common decisionmaker, agreement, command channel, or coordinated action has been identified. |

### Packet 4 — access, amplification, and Dialog

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `PA-01` | FACT / ARCHITECTURE | **ESTABLISHED AS PUBLIC AMPLIFICATION — ADVANCE CAUTIOUSLY.** Bannon's media apparatus applied public pressure in the 2025 AI-moratorium fight; the moratorium was removed 99–1. A separate source also records his advocacy during the Speaker contest. | `SRC-PA-008`, `SRC-PA-009`, `SRC-PA-010`, `SRC-PA-011`; secondary instance `SRC-PA-001` | The broad coalition, amendment record, and roll call do not isolate Bannon's causal contribution or prove a private backchannel. |
| `PA-02` | CAUSAL JOIN | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** | `LOG-01`, `SRC-PA-001`, `SRC-PA-008`–`011` | Public pressure is not command of administration policy. |
| `PA-03` | FACT / ARCHITECTURE | **ESTABLISHED AS REPORTED PROXIMITY, BOUNDED IN TIME — ADVANCE CAUTIOUSLY.** Johnson and Berger shared a donor-owned residence in early 2025. | `SRC-PA-002`, `SRC-PA-003` | Preserve spokesperson denial of policy talks and fair-market-rent position; relocation ends the reported period. |
| `PA-04` | CAUSAL JOIN | **OPEN — HOLD.** No recovered record ties Berger to a specific Johnson decision. | `SRC-PA-002`, `REQ-PA-02` | Need dated advice/request → scheduling/contact → action → consequence. |
| `PA-05` | FACT | **ESTABLISHED AS SECONDARY REPORTING — ADVANCE.** Johnson relocated roughly one month later. | `SRC-PA-003` | Move does not establish motive or concede earlier influence. |
| `PA-06` | ARCHITECTURE | **ESTABLISHED AT PRIVATE-ACCESS AND COMMON-FOUNDER LEVEL — ADVANCE.** Dialog is a private curated network; Thiel is reported as a Dialog co-founder and is Palantir co-founder/chairman. | `SRC-PA-004`, `SRC-PA-005`, `SRC-PA-006` | WIRED and derivative retellings share one leak; common founder does not establish procurement influence, instruction, or command. |
| `PA-07` | FACT | **RETIRED/CORRECTED — CLOSE.** Scheduled/registered 2026 Powerscourt co-attendance cannot be stated; event was cancelled before the planned dates. | `SRC-PA-004`, `SRC-PA-007` | Registration ≠ attendance; cancellation defeats the event-based join. |
| `PA-08` | CAUSAL JOIN | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** | `LOG-01`, `SRC-PA-004`–`007`, `REQ-PA-03` | Need communication/agenda → shared decision → attributable action; secrecy, session titles, and proximity are insufficient. |

### Packet 5 — judiciary and Congress

| Claim | Finding type | Source-bearing disposition and action | Attached source IDs | Boundary / next discriminating test |
|---|---|---|---|---|
| `JU-01` | FACT / ARCHITECTURE | **ESTABLISHED — ADVANCE.** Leo and associated networks played documented selection and confirmation-advocacy roles. | `SRC-JU-001`, `SRC-JU-009` | No post-confirmation control follows. Self-description and ProPublica reporting are separate source types, not proof of command. |
| `JU-02` | FACT / ARCHITECTURE | **ESTABLISHED — ADVANCE.** Senate leadership exercised decisive scheduling/procedural gatekeeping across Garland and later nominations. | `SRC-JU-002`, `SRC-JU-003`, `SRC-JU-004` | This is constitutional/institutional power, not misconduct by itself. |
| `JU-03` | FACT / ARCHITECTURE | **ESTABLISHED AT ANNOUNCED ADVOCACY LEVEL — ADVANCE CAUTIOUSLY.** JCN publicly announced multimillion-dollar confirmation efforts. | `SRC-JU-005`, `SRC-JU-006`, `REQ-JU-01` | JCN is an interested self-report; exact expenditures and funding chains require filings/invoices. Advocacy is not justice control. |
| `JU-04` | FACT / ARCHITECTURE | **ESTABLISHED — ADVANCE.** Marble received roughly $1.604B in reported contributions; source-bearing reporting identifies the Seid/Tripp Lite route. | `SRC-JU-007`, `SRC-JU-008` | Separate filing fact from donor identification; no retroactive use of later funds. |
| `JU-05` | CAUSAL JOIN | **RETIRED/CORRECTED — CLOSE.** The Seid/Marble transfer did not fund the named Gorsuch/Kavanaugh/Barrett confirmation campaigns on the recovered chronology. | `SRC-JU-002`, `SRC-JU-007`, `SRC-JU-008` | Gorsuch/Kavanaugh predate Marble transfer; Barrett was confirmed before the 2021 sale. A different date-specific funding instrument would be required. |
| `JU-06` | FACT / LEGAL ELEMENT | **ESTABLISHED AS BENEFITS/ACCESS AND DISCLOSURE HISTORY; CONSEQUENCE OPEN — ADVANCE CAUTIOUSLY.** | `SRC-JU-010`, `SRC-JU-011`, `SRC-JU-012`, `SRC-JU-018`, `SRC-LAW-006`, `SRC-JU-016` | Preserve Thomas/Crow explanations and legal dispute. No payment-for-outcome or case-specific influence is established. |
| `JU-07` | FACT / LEGAL ELEMENT | **ESTABLISHED AS TRAVEL/ACCESS AND LATER CASE INTERSECTION; RECUSAL QUESTION OPEN — ADVANCE CAUTIOUSLY.** | `SRC-JU-013`, `SRC-JU-019`, `SRC-LAW-006`, `SRC-JU-016` | Preserve Alito's position and 7–1 NML Capital result. No purchased vote. |
| `JU-08` | FACT / LEGAL ELEMENT | **ESTABLISHED AS PROPERTY TRANSACTION AND LATER FIRM/court INTERSECTION; FAVORABLE TREATMENT NOT ESTABLISHED — ADVANCE CAUTIOUSLY.** | `SRC-JU-014`, `SRC-JU-020`, `SRC-JU-021`, `SRC-LAW-006`, `SRC-JU-016` | Preserve Duffy's no-contact/ethics-consultation account. Do not use crude win/loss ratios as proof. |
| `JU-09` | CAUSAL JOIN / LEGAL ELEMENT | **OPEN — HOLD.** Jane Roberts recruiting presents a disclosure/recusal question, but the required chain is absent. | `SRC-JU-017`, `SRC-JU-022`, `SRC-JU-023`, `REQ-JU-03` | Need commission → firm/client → case → Chief Justice knowledge/participation → recusal analysis. Advisory Opinion 107 defeats an automatic-recusal shortcut. |
| `JU-10` | FACT / NULL RESULT | **NOT ESTABLISHED — CLOSE ON CURRENT RECORD.** No comparable personal-benefactor/financial-capture chain for Kavanaugh or Barrett was recovered in this selected sample. | `LOG-01`, `SRC-JU-015` | Bounded null result, not a control or proof of universal absence; ordinary disclosed income is not capture. |
| `JU-11` | ARCHITECTURE | **ESTABLISHED — ADVANCE.** Outside selection/advocacy, presidential nomination, Senate gatekeeping, and life-tenured office form a durable institutional route. | `SRC-JU-001`–`006`, `SRC-JU-002/003` | Durability follows tenure/sequence; no central command, ownership of votes, or abnormality claim without comparison data. |

### Packet U — known-live preservation rows

These rows are intentionally not promoted by newly found headlines. They require component-level adjudication against the controlling register.

| Claim | Finding type | Disposition and action | Located lead / missing instrument | Hard boundary |
|---|---|---|---|---|
| `U-01` WorldClaw/WLF AI arrangement | FACT / LEGAL ELEMENT | **INDETERMINATE — HOLD.** | `REQ-U-01`: Reuters item, corporate records, adviser identity, transaction terms, legal instrument | “No indication of illegality” is not a legal finding; do not state an adviser identity without verification. |
| `U-02` OCC trust-bank charter | FACT / LEGAL ELEMENT | **INDETERMINATE — HOLD.** | `REQ-U-02`: OCC conditional-approval/charter instrument and conditions | Reporting about an application/conditional approval is not the charter itself. |
| `U-03` MGX/Abu Dhabi specificity | FACT | **INDETERMINATE — HOLD FOR COMPONENT REVIEW.** | `SRC-TC-006`, `SRC-TC-007`; `REQ-U-03` transaction documents | Do not merge announcement, USD1 settlement reporting, and pardon into one causal brick. |
| `U-04` Rubio/State Palantir orders | FACT / CAUSAL JOIN | **INDETERMINATE — HOLD.** | `REQ-U-04`: award/task-order/SOW and person-level participation | No cross-agency command from a reported order. |
| `U-05` Treasury/IRS Palantir work | FACT / CAUSAL JOIN | **INDETERMINATE — HOLD.** | `REQ-U-05`: award, privacy, API/integration, §6103 records | Do not force Treasury/IRS and ICE into one system absent an actual data or command join. |
| `U-06` Clark Minor/HHS | FACT / CAUSAL JOIN | **INDETERMINATE — HOLD.** | `SRC-PL-019`; `REQ-U-06` agency-held filing and participation records | Employment/holdings chronology is not approval of CMS/ICE sharing. |
| `U-07` Bondi disclosure | FACT / SYMBOLIC LEAD | **INDETERMINATE — HOLD; SYMBOLIC DATE CLAIM CUT.** | `REQ-U-07`: official disclosure package and primary dates | Date symmetry has zero evidentiary weight. |
| `U-08` adult-child crypto gifts / CDs | FACT / LEGAL ELEMENT | **INDETERMINATE — HOLD AS TWO-SIDED COUNTEREVIDENCE.** | `SRC-CR-004`, `SRC-LAW-003`; `REQ-U-08` transaction, retained-interest, agency request, CD, and ethics analysis | Gifts are not automatically suspicious, evasive, exculpatory, or legally sufficient. Do not assume a CD exists. |

## 4. Actual joins and absent joins

### Demonstrated narrow joins

| Join | Disposition | Source IDs | Exact limit |
|---|---|---|---|
| `J-01` Faith Office ↔ DOJ/AG | **ESTABLISHED** | `SRC-RP-001`–`004` | Public institutional route only; no improper preference. |
| `J-02` Blanche disclosure/ethics ↔ dated memo ↔ later divestiture | **ESTABLISHED AS CHRONOLOGY** | `SRC-CR-001`–`004` | Does not resolve §208, authorization, or intent. |
| `J-03` CMS/HHS ↔ ICE ↔ Palantir | **ESTABLISHED AT CUSTODY LEVEL** | `SRC-PL-008`, `009`, `012` | Does not establish ELITE ingestion or enforcement use. |
| `J-04` Palantir ↔ multiple official federal contracts | **ESTABLISHED WITH ENUMERATED SCOPE** | `SRC-PL-001`–`005` | Shared vendor is not shared agency or command. |
| `J-05` Leo network ↔ nomination/confirmation architecture | **ESTABLISHED** | `SRC-JU-001`–`006` | No post-confirmation control or purchased judgment. |
| `J-06` Bannon media pressure ↔ AI-moratorium legislative environment | **ESTABLISHED AS PUBLIC AMPLIFICATION; CONSEQUENCE NOT ISOLATED** | `SRC-PA-008`–`011` | Broad coalition and 99–1 vote prevent causal primacy; no hidden command. |

### Joins not established

- Faith Office ↔ Blanche as a common hidden command.
- Leo network ↔ Palantir contracting or data custody.
- Dialog membership/registration ↔ a Palantir award or government decision.
- Bannon ↔ Blanche as a command relationship.
- White-Cain ↔ Leo as a hierarchy.
- Seid/Marble ↔ Trump-family crypto.
- WLF transaction ↔ Zhao pardon as consideration or cause.
- Supreme Court benefactors ↔ administration command.
- Johnson/Berger proximity ↔ a specific legislative action.
- CMS dataset custody ↔ a particular enforcement output.

## 5. Null results, counterevidence, and retired arrows

### Bounded null results

`LOG-01` records a review of the supplied corpus, its extracted raw PDF, the recovered public instruments in this register, and targeted public-source recovery on 17 Aug. 2026. It is an internal audit log, class `X`, not an external source and not proof of universal absence.

- `CR-09`: no direct consideration, payment, coordinated trade, bribery, or intentional-self-enrichment evidence recovered.
- `PL-07`: no disputed Medicaid-dataset → ELITE ingestion/query → person-level enforcement result recovered.
- `PL-11`: no Barbaccia → Palantir steering or matter-specific participation recovered.
- `PL-14`: no common Palantir command across agencies recovered.
- `PA-02`: no Bannon command of administration policy recovered.
- `PA-08`: no Dialog-coordinated common government decision recovered.
- `JU-10`: no comparable personal financial-capture chain for Kavanaugh or Barrett recovered in the selected sample.

These are **NULL RESULTS**, not “negative controls,” exonerations, or no-record certifications.

### Mandatory counterevidence

- Faith route: formal interagency religious-liberty administration is an ordinary executive function unless selective benefit/exclusion is shown.
- Blanche: DOJ reportedly says the issue was flagged/addressed/cleared in advance; a regulatory exemption or no-covered-matter analysis may require no individualized waiver; reported adult-child gifts may extinguish some imputed interests if valid and complete.
- Crypto policy: structural coexistence is not motive; reporting aggregates share one OGE filing family.
- ICE procurement: proprietary migration/interoperability needs may lawfully support limited/sole sourcing; the 2022 procurement record is internally mixed and must be reconciled.
- Medicaid data: government representations said no ingestion/use at stated dates; Palantir said the dataset was purged; a Teams transfer cuts against an inference of integrated ELITE ingestion even while raising custody concerns.
- Barbaccia: a formal PAS ethics agreement may be the wrong instrument; future return was not completed at cutoff.
- Patel: required divestiture was reported; neither that sale nor the prior holding proves participation.
- Johnson/Berger: spokesperson said fair-market rent and no policy conversations; move-out bounded the co-residence period.
- Dialog: a genuine leak can contain an identity error; WIRED corrected a Jeff Epstein conflation. Registration is not attendance, and the event was cancelled.
- Seid/Marble: chronology defeats the attractive direct-confirmation-funding arrow.
- Thomas/Crow: Thomas's “personal hospitality/family trips” position and later amendments must remain adjacent to the allegation.
- Alito/Singer: Alito disputed disclosure/recusal claims; NML Capital was 7–1, weakening a bespoke-vote theory.
- Gorsuch/Duffy: Duffy said he had not met/spoken with Gorsuch and consulted firm ethics personnel.

### Retired or corrected arrows

- Project crypto total/range of `$580M–$1.4B+`: **retired**; denominators differ. `TC-01` remains indeterminate.
- Dataset custody → ELITE ingestion/target/arrest/removal: **not established**.
- Barbaccia appointed in May 2026: **corrected** to 19 Feb. 2026; 7 May was a page update.
- Barbaccia returned to Palantir before cutoff: **retired**; it was a reported future plan.
- Barbaccia retained PLTR stock: **unsupported/held**.
- Patel's sale exonerates him: **retired**; it is mitigation, not exoneration.
- 2026 Dialog/Powerscourt actual co-attendance: **retired**; event cancelled.
- WIRED Dialog investigation was retracted: **corrected** to a narrow identity-disambiguation correction.
- Guardian retracted Dialog reporting: **do not state** absent an actual notice.
- Seid's $1.6B funded Gorsuch/Kavanaugh/Barrett confirmations: **retired on chronology**.
- Johnson/Berger proximity was ongoing: **corrected** with a March 2025 endpoint.
- No response/not found = instrument does not exist: **prohibited conversion**.
- “Four true bills, three no-bills” from the legacy indictment: **discarded as irreproducible**; the numbered counts do not yield that arithmetic.

## 6. Missing-instrument queue

| Request ID | Discriminating instrument | Claims affected |
|---|---|---|
| `REQ-RP-01` | Specific outside request/recommendation, pre-decision contacts, resulting grant/contract/enforcement action, comparator, and governing exception | `RP-06` |
| `REQ-CR-01` | Case-specific §208 route: written waiver if any; Part 2640 exemption analysis; no-covered-particular-matter/no-direct-effect analysis; recusal/screening advice; decisionmaker/scope | `CR-06`–`CR-08` |
| `REQ-TC-01` | Page-level recalculation of `SRC-TC-001` with inclusion/exclusion taxonomy | `TC-01` |
| `REQ-TC-02` | Clemency recommendations, lobbying/contact logs, communications, consideration/transaction records | `TC-04` |
| `REQ-PL-01` | Complete 2022 and later ICE J&As, market research, alternatives, source-selection and migration/IP record; reconcile one-source/fair-opportunity coding | `PL-04` |
| `REQ-PL-02` | Dkt. 182 attachments, transfer/deletion logs, copy inventory, ELITE ingestion/query logs, audit trail, and person-level enforcement outputs | `PL-06`–`PL-08` |
| `REQ-PL-03` | Barbaccia OMB/GSA 278e, 278-Ts, recusal/screening/§208 and post-employment advice, waivers if any, termination report, Palantir-specific participation, actual post-31 Aug. employment | `PL-09`–`PL-11` |
| `REQ-PL-04` | Patel recusal/participation, approval, agenda, procurement, and communication records; CD and agency request if any | `PL-12`, `PL-13` |
| `REQ-PA-02` | Berger request/advice, Johnson contact/scheduling record, resulting action, and comparator | `PA-04` |
| `REQ-PA-03` | Dialog communications/agenda tied to a shared decision and subsequent attributable action | `PA-08` |
| `REQ-JU-01` | JCN audited expenditures, invoices, ad buys, grant/funding transfers with dates and campaign assignment | `JU-03`, `JU-05` |
| `REQ-JU-02` | Individual justice disclosures, underlying travel/property records, case-party/amicus chronology, knowledge, and recusal analysis | `JU-06`–`JU-08` |
| `REQ-JU-03` | Jane Roberts commission → client/firm → Supreme Court case → Chief Justice knowledge/participation → recusal chain | `JU-09` |
| `REQ-U-01`–`REQ-U-08` | Exact instruments named in the Packet U table | `U-01`–`U-08` |

## 7. Source-family concentration and comparison controls

| Corridor | Concentration | Consequence for claim state |
|---|---|---|
| Blanche | OGE primary family supplies holdings/transactions; ProPublica is the sole recovered carrier of DOJ's clearance assertion | Clearance is established only as an attributed position; legal conclusion remains open. |
| Trump crypto aggregate | Reuters and AP both derive amounts from the same OGE filing but apply different taxonomies | Count one underlying document family, two interpretations; do not average or range them. |
| Medicaid custody | Court order/party filings/declarations are one docket family; NPR/KCLU reports from that family and adds party statements | Strong for custody route, weak for “independent-source count”; downstream use remains unestablished. |
| Dialog | WIRED and many retellings share one leaked roster; Axios is independent only for existence/founding; RTÉ is separate for cancellation | Roster repetitions do not multiply corroboration; no action join. |
| Judicial benefits | Several rows depend heavily on ProPublica's reporting and linked records | Treat each underlying trip/property/disclosure as a separate component, but do not count ProPublica stories as independent outlets. |
| JCN spending | JCN self-reports its own campaigns | Establishes announced activity, not audited expenditure; keep interested-source flag. |

The selected actor set is non-random. Symbolic material influenced historical selection but carries zero evidentiary weight here. Therefore this register makes no prevalence, exceptionalism, unusualness, or population claim without an external comparison class. An event may be established without a base rate; a claim that it is abnormal may not.

## 8. Namespace and scope controls

- Canonical `PL-01`–`PL-14` are the human-side Palantir rows above.
- The legacy Conduct Docket's different `PL-01`–`PL-04` propositions must be namespaced `CD-PL-01`–`CD-PL-04`; they may not overwrite or silently corroborate canonical rows.
- OpenAI governance, copyright, and energy lanes in the Conduct Docket remain supplemental and outside this paper. They are not cross-packet joins to the human-side corridors merely because some actors or vendors recur.
- Filing-packet requests are acquisition targets, not evidence. A scoped no-record response would establish only the responding office's search result for the stated scope, custodians, and period.

## 9. Publication do-not-state boundary

Do not state, on this record:

- a unified cabal, hidden priesthood, occult/bloodline lineage, single command center, or conspiracy;
- a secret Palantir command spanning agencies;
- that Blanche violated §208 as an adjudicated fact, accepted a bribe, or intentionally enriched himself;
- that WLF purchased the Zhao pardon;
- that Barbaccia steered procurement, retained stock, or had already returned to Palantir by the cutoff;
- that Patel influenced a Palantir matter;
- that the disputed Medicaid data entered ELITE or generated a target, arrest, detention, or removal;
- that the 2026 Powerscourt Dialog retreat occurred or its registrants attended together;
- that Johnson acted because of Berger, or that Bannon commanded policy;
- that Dialog coordinated a government decision;
- that Seid's $1.6B funded the three named Trump Supreme Court confirmations;
- that Crow, Singer, or Duffy purchased a judicial outcome;
- that Kavanaugh or Barrett was personally financially captured;
- any Guardian retraction that is not evidenced by an actual correction notice;
- WorldClaw legality or adviser claims not grounded in the missing primary/source-bearing record;
- an official project crypto total of $580M, ~$1.2B, >$1.4B, or a range connecting them.

---

**Registry conclusion:** The record supports multiple separately documented institutional corridors and several narrow joins. It does not support a unified command theory. Every stronger causal, legal, or intent claim remains tied to a named missing instrument or is closed on the current record.

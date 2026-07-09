# Domain map — the 8 Jerry-Area business domains

Each domain has an archetype **hero (A2)**, an **A3 squad**, and folder indices that
**differ between the corpus tree and the Area tree**. Resolve carefully.

| Domain | Hero (A2) | Squad (A3) | Corpus folder (`01_Guides/`) | Area folder (`B2_Area_Domains/`) | Status (2026-05-31) |
|---|---|---|---|---|---|
| Growth | Superman | Guardians of the Galaxy | `07_Growth` | `01_Growth_Superman_Guardians` | ✅ 18 (SHADOW_ACTIVE) |
| Sales | Martian Manhunter / John Jones | Illuminati | `06_Sales` | `02_Sales_MartianManhunter_Illuminati` | ✅ 14 (CANONICAL v2 — +MDW/SPIN/Gap/Challenger/Voss ; v3 = Dan Martell) |
| Product | Flash | The Avengers | `01_Product` | `03_Product_Flash_Avengers` | ✅ 18 (CANONICAL) |
| Ops | Batman | Fantastic Four | `02_Ops` | `04_Ops_Batman_Fantastic4` | ✅ 22 (CANONICAL, v2) |
| IT | Cyborg | Kang Dynasty | `03_IT` | `05_IT_Cyborg_KangDynasty` | ✅ 18 (CANONICAL — corpus 322 + Kang canon) |
| Finance | Wonder Woman | Thunderbolts | `04_Finance` | `06_Finance_WonderWoman_Thunderbolts` | ✅ 12 (CANONICAL_FROM_CANON — corpus externe vide) |
| Legal | Aquaman | Eternals | `05_Legal` | `08_Legal_Aquaman_Eternals` | ✅ 12 (CANONICAL_FROM_CANON — corpus externe vide) |
| People | Green Lantern | X-Men | `08_People` | `07_People_GreenLantern_XMen` | ✅ 12 (CANONICAL_FROM_CANON — corpus externe vide) |

> ⚠️ The Area-tree index is NOT the corpus-tree index (e.g. Ops = corpus `02_Ops`
> but Area `04_Ops…`; Sales = corpus `06_Sales` but Area `02_Sales…`). Always
> resolve by name, then confirm the exact folder by listing — don't assume the
> number. The B0_Self_Operating_Business_Doctrine note: People→`07`, Legal→`08` in
> the Area tree even though their canon SOA numbers differ. List to confirm.

## Path roots

```
ASPACE = C:/Users/amado/ASpace_OS_V2          # Unix-style for Bash (no apostrophe)
CORPUS = $ASPACE/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides
AREA   = $ASPACE/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains
QUEUE  = $ASPACE/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/skills_queue.md
```

## Doctrine filename convention

`03_<HERO_UPPER>_<DOMAIN_UPPER>_PRINCIPLES.md`
- Growth → `03_SUPERMAN_GROWTH_PRINCIPLES.md`
- Ops → `03_BATMAN_OPS_PRINCIPLES.md`
- Sales → `03_JOHNJONES_SALES_PRINCIPLES.md` (hero short name John Jones, not Martian Manhunter, for the filename — match the existing file).

Each domain folder also already contains scaffolding you must read for grounding:
`00_B2_DOMAIN_CONTROL_ROOM.md` (KRs, North Star, reserved decisions),
`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`, `02_B3_SWARM_SUPERVISION_PROTOCOL.md`,
`README.md`, and `B3_Squad_<Squad>/00_B3_SQUAD_CANON.md` (the canon roster).

## Grounded specifics worth reusing

- **Sales North Star / KRs** (from control room): close rate KR-2a >30% on qualified
  leads; deal size KR-2b ≥$10K/$25K/$50K by mode; cycle KR-2c <30/<90d; concentration
  KR-2d <20%. Illuminati roster (canon Notion): Black Bolt (closer), Iron Man (demo/ROI),
  Mr Fantastic (discovery), Namor (negotiation), Professor X (objection-read),
  Doctor Strange (forecast/qualification). Lead character = Black Bolt.
- **Growth** North Star: ICP-qualified opportunities from non-paid channels. KR-4a..d.
- **Ops** North Star: the autonomy ratio ("business runs without you"). DEAL spine.
  Invisible Woman = grounded Build Gate ("Filtre Invisible Woman" in the Airtable 🦇 adapter).
- **Cross-domain backlog already on disk**: `06_Sales/DAN_MARTELL_AUDIT.md` indexes
  ~97 Dan Martell videos classified across all 8 domains (Sales 28, People 24, IT 15,
  Finance 13, Product 5, Ops 3, Growth 7, Legal 2). It's an index, not content — use
  it to seed each domain's v2 backlog, not as a distillation source.

## Lesson (2026-05-31): empty external corpus ≠ no doctrine

Finance, People, Legal had EMPTY external Geordi guide folders — but their `B3_Squad_*/00_B3_SQUAD_CANON.md` + control-room KRs are RICH internal canon (members, stack, SOPs, KPIs, gates, anti-patterns). Distill `CANONICAL_FROM_CANON` from that internal canon (honestly labeled, external corpus pending) instead of writing a PENDING scaffold. Only write PENDING if BOTH external corpus AND squad canon are empty.

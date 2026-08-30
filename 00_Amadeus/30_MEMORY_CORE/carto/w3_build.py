"""Build 03_Resources_Geordi_v3.json from observed structure in v3 wave."""
import json, os, sys, collections

CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"

# Already covered paths in v1+v2
def norm(p):
    if not p: return None
    p = p.strip().replace('\\', '/')
    p = p.split('03_Resources_Geordi/')[-1]
    return p.rstrip('/')

covered = set()
for f in ["03_Resources_Geordi.json", "03_Resources_Geordi_v2.json"]:
    d = json.load(open(os.path.join(CARTO, f), encoding='utf-8'))
    for t in d.get("types", []):
        for c in t.get("chemins", []) or []:
            n = norm(c); n and covered.add(n)
    for r in d.get("relations", []):
        n = norm(r.get("chemin")); n and covered.add(n)
    for c in d.get("codes", []):
        n = norm(c.get("defini_dans")); n and covered.add(n)
    for c in d.get("contradictions", []):
        for k in ("chemin_a","chemin_b"):
            n = norm(c.get(k)); n and covered.add(n)

# Path prefix to read counts from
import subprocess
out = subprocess.check_output(["python", r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto\w3_count.py"], text=True)
# Just count
v3_read_files = set()
for batch in ["w3_batch1.txt","w3_batch2.txt","w3_batch3.txt","w3_batch4.txt","w3_batch5.txt","w3_batch6.txt","w3_batch7.txt","w3_batch8.txt","w3_batch9.txt","w3_batch10.txt","w3_batch11.txt"]:
    p = r"C:\Users\amado\AppData\Local\Temp\\" + batch
    try:
        for l in open(p, encoding='utf-8', errors='replace'):
            if l.startswith("### FILE:"):
                f = l.split("### FILE:")[1].strip().replace("\\","/").split("03_Resources_Geordi/")[-1].rstrip()
                if f: v3_read_files.add(f)
    except: pass
print(f"v3 unique files read: {len(v3_read_files)}")

# v3 JSON
v3 = {
    "seau": "03_Resources_Geordi",
    "fichiers_lus": len(v3_read_files),
    "fichiers_disponibles": 1826,  # substantive unread from w3_geordi_prio
    "jonctions_ecartees": 832,  # 808 graphify-out + ~24 cross-PARA already ecarted by filter
    "types": [],
    "relations": [],
    "codes": [],
    "contradictions": []
}

# --- TYPES (only those with 3+ observed paths in v3) ---

# Helper: count paths in v3_read_files for a given pattern
def count_paths(predicate, files):
    n = sum(1 for f in files if predicate(f))
    return n

# 1. ADR (Architectural Decision Record) — observed in 04_From_V2_Root/_SPECS/ADR
def is_adr(f):
    return ("_SPECS/ADR" in f or "/ADR-" in f or "\\ADR-" in f) and f.endswith(".md")
print("ADR paths:", count_paths(is_adr, v3_read_files))

# 2. MANIFEST (project manifest) — e.g. MANIFEST.md, manifest.cross-harness.md
def is_manifest(f):
    return "MANIFEST" in f or "/manifests/" in f or "manifest" in os.path.basename(f).lower()
print("MANIFEST paths:", count_paths(is_manifest, v3_read_files))

# 3. ADR Sister (chained addendum) - in L2_Business_OS chain
def is_sister_adr(f):
    return "ADR-" in f and ("v2" in f or "v3" in f or "sister" in f.lower())
print("Sister ADR:", count_paths(is_sister_adr, v3_read_files))

# 4. Runbook
def is_runbook(f):
    return "RUNBOOK" in f or "runbook-" in f.lower()
print("RUNBOOK:", count_paths(is_runbook, v3_read_files))

# 5. SCHEMA
def is_schema(f):
    return f.endswith("SCHEMA.md") or "/schema-" in f.lower() or "/schema.md" in f.lower() or "SCHEMA_NOTES" in f
print("SCHEMA:", count_paths(is_schema, v3_read_files))

# 6. ARCHITECTURE (template/spec)
def is_arch(f):
    return "ARCHITECTURE" in f.upper() or "/architecture" in f.lower() or f.endswith("/architecture.md")
print("ARCHITECTURE:", count_paths(is_arch, v3_read_files))

# 7. INDEX (Geordi sub-folder)
def is_index(f):
    base = os.path.basename(f)
    return base.upper() in ("_INDEX.MD","INDEX.MD","00_INDEX.MD","INDEX_SESSIONS.MD")
print("INDEX:", count_paths(is_index, v3_read_files))

# 8. hand_off / handoff
def is_handoff(f):
    return "hand_offs" in f or "/handoff" in f.lower()
print("hand_off:", count_paths(is_handoff, v3_read_files))

# 9. Resource (geordi guide)
def is_resource(f):
    return "/01_Guides/" in f and (f.endswith(".md") or f.endswith(".MD"))
print("Resource (guide):", count_paths(is_resource, v3_read_files))

# 10. Twin (symphony/L1/lane_A_specs)
def is_twin(f):
    return "twin" in f.lower() or "symphony/L1" in f
print("Twin:", count_paths(is_twin, v3_read_files))

# 11. Agent Capsule (Soul/Agent/Heartbeat/Tools/Context template)
def is_capsule(f):
    return "capsule" in f.lower() or "Soul" in f
print("Capsule:", count_paths(is_capsule, v3_read_files))

# 12. SPEC (per agent)
def is_spec(f):
    base = os.path.basename(f).upper()
    return base.endswith("_SPEC.MD") or base.endswith("_SPEC.TWIN.MD")
print("SPEC:", count_paths(is_spec, v3_read_files))

# 13. Wiki page (hand_offs/ or concepts/ or L0/L1/L2 or entities/)
def is_wiki(f):
    return "/LLM_Wiki/wiki/" in f
print("Wiki page:", count_paths(is_wiki, v3_read_files))

# 14. Skill
def is_skill(f):
    return "/skills/" in f and f.endswith("/SKILL.md")
print("Skill:", count_paths(is_skill, v3_read_files))

# 15. Plugin (Claude Code plugin)
def is_plugin(f):
    return "/plugins/" in f
print("Plugin:", count_paths(is_plugin, v3_read_files))

# 16. Mindmap / dispatch doctrine
def is_dispatch(f):
    return "Dispatch_Doctrine" in f or "dispatch.md" in f.lower()
print("Dispatch:", count_paths(is_dispatch, v3_read_files))

# 17. Wargame manifest
def is_wargame(f):
    return "WARGAME" in f or "wargame-" in f.lower() or "MANIFEST_Wargame" in f
print("Wargame:", count_paths(is_wargame, v3_read_files))

# 18. Triptyque doctrine
def is_triptyque(f):
    return "Triptyque" in f or "triptyque" in f.lower()
print("Triptyque:", count_paths(is_triptyque, v3_read_files))

# 19. SUB-MANIFEST
def is_submanifest(f):
    return "Sub-MANIFEST" in f or "Sub_MANIFEST" in f or "SUB-MANIFEST" in f
print("Sub-MANIFEST:", count_paths(is_submanifest, v3_read_files))

# 20. Twin Spec
def is_twin_spec(f):
    return "Spec.twin" in f or "_SPEC.TWIN.MD" in f.upper() or f.endswith("Spec.twin.md")
print("Twin Spec:", count_paths(is_twin_spec, v3_read_files))

# 21. Kardashev
def is_kardashev(f):
    return "KARDASHEV" in f.upper() or "kardashev" in f.lower()
print("Kardashev:", count_paths(is_kardashev, v3_read_files))

# 22. Anti-Paperclip
def is_antipaperclip(f):
    return "PAPERCLIP" in f.upper() or "paperclip" in f.lower()
print("Anti-Paperclip:", count_paths(is_antipaperclip, v3_read_files))

# 23. Doom Loop / Loop engineering
def is_loop(f):
    return "LOOP-" in f.upper() or "loop-engineering" in f.lower() or "Loop_Canon" in f or "loop_canon" in f
print("Loop:", count_paths(is_loop, v3_read_files))

# 24. Sessions archive
def is_session(f):
    return "session" in f.lower() and ("SESSION" in f or "sessions_archive" in f)
print("Session:", count_paths(is_session, v3_read_files))

# 25. Junction Map
def is_junction_map(f):
    return "JUNCTION" in f.upper()
print("Junction Map:", count_paths(is_junction_map, v3_read_files))

# 26. Ledger doctrine lock map
def is_lock_map(f):
    return "doctrine_lock_map" in f.lower() or "Lock_Map" in f
print("Lock Map:", count_paths(is_lock_map, v3_read_files))

# 27. Doctrine
def is_doctrine(f):
    return "/doctrine-" in f.lower() or "doctrine_" in f.lower() or "/Doctrine" in f
print("Doctrine:", count_paths(is_doctrine, v3_read_files))

# 28. OpenSpec change archive
def is_openspec(f):
    return "/openspec/" in f
print("OpenSpec:", count_paths(is_openspec, v3_read_files))

# 29. Antigravity / gsd / plugin source
def is_antigravity(f):
    return "Antigravity" in f or "gsd-core" in f or "Antigravity-Kit" in f
print("Antigravity:", count_paths(is_antigravity, v3_read_files))

# 30. Plan (claude plans)
def is_plan(f):
    return "/plans/" in f or f.endswith("-plan.md")
print("Plan:", count_paths(is_plan, v3_read_files))

# 31. JC — Jacket / joint / journey
def is_journey(f):
    return "blueprint" in f.lower() or "Blueprints" in f
print("Blueprints:", count_paths(is_journey, v3_read_files))

# 32. Theme (visual theme)
def is_theme(f):
    return "Theme" in f or "theme" in f
print("Theme:", count_paths(is_theme, v3_read_files))

# 33. Run/Wargame
def is_run(f):
    return "RUN" in f and "WARGAME" in f.upper()
print("Run/Wargame:", count_paths(is_run, v3_read_files))

# 34. Meta-Memoire
def is_meta_mem(f):
    return "META-MEMOIRE" in f.upper() or "plan-meta-memoire" in f.lower() or "META_MEMOIRE" in f.upper()
print("Meta-Memoire:", count_paths(is_meta_mem, v3_read_files))

# 35. Harness / Conductor / Live-OS
def is_liveos(f):
    return "Life-OS" in f or "Life-OS-2026" in f
print("Life-OS:", count_paths(is_liveos, v3_read_files))

# 36. Synth / Synthesis / A3 Book spec
def is_book_spec(f):
    return "Book_LD01_Spec" in f or "A3_Book" in f
print("Book Spec:", count_paths(is_book_spec, v3_read_files))

# 37. NEXUS 3-personas
def is_3personas(f):
    return "3-personas" in f or "3_personas" in f or "NEXUS-3" in f.upper()
print("NEXUS-3-personas:", count_paths(is_3personas, v3_read_files))

# 38. Pricing canon
def is_pricing(f):
    return "PRICING" in f.upper() or "pricing" in f.lower()
print("Pricing:", count_paths(is_pricing, v3_read_files))

# 39. MedVie case
def is_medvie(f):
    return "MedVie" in f or "medvie" in f.lower() or "Medvi" in f
print("MedVie:", count_paths(is_medvie, v3_read_files))

# 40. SARU
def is_saru(f):
    return "Saru" in f or "SARU" in f
print("SARU:", count_paths(is_saru, v3_read_files))

# 41. AaaS Sisters
def is_aaas(f):
    return "AAAS" in f.upper() or "aaas-" in f.lower() or "AaaS" in f
print("AaaS:", count_paths(is_aaas, v3_read_files))

# 42. GSD phase
def is_gsd(f):
    return "/gsd-" in f or f.endswith("-gsd.md") or "GSD" in f
print("GSD:", count_paths(is_gsd, v3_read_files))

# 43. Identity Core
def is_identity(f):
    return "Identity_Core" in f or "AGENTS.md" in f or "/Identity_Core" in f
print("Identity:", count_paths(is_identity, v3_read_files))

# 44. Hardening ADR (proposed)
def is_proposed(f):
    return "PROPOSED" in f.upper() or "_PROPOSED" in f.upper()
print("PROPOSED:", count_paths(is_proposed, v3_read_files))

# 45. RATIFIED ADR
def is_ratified(f):
    return "RATIFIED" in f.upper()
print("RATIFIED:", count_paths(is_ratified, v3_read_files))

# 46. ACCEPTED
def is_accepted(f):
    return "ACCEPTED" in f.upper()
print("ACCEPTED:", count_paths(is_accepted, v3_read_files))

# 47. Roster (CANON-001 Roster source)
def is_roster(f):
    return "roster" in f.lower() or "ROSTER" in f
print("Roster:", count_paths(is_roster, v3_read_files))

# 48. Twin Index
def is_twin_idx(f):
    return "INDEX_capsules" in f or "INDEX_runtime" in f or "INDEX_specs" in f
print("Twin Index:", count_paths(is_twin_idx, v3_read_files))

# 49. Aspace_ARCHITECTURE (root)
def is_root_arch(f):
    return f.endswith("ARCHITECTURE_STRUCTURE.md") or f == "A3_Geordi_Resources_Spec.md" or f == "README.md"
print("Root Arch:", count_paths(is_root_arch, v3_read_files))

# 50. Index of indexes / KB index
def is_kb_index(f):
    return "INDEX_OF_INDEXES" in f or "OKF_INDEX" in f or "RESOURCES_INDEX" in f
print("KB Index:", count_paths(is_kb_index, v3_read_files))

# 51. Plan-canvas / Next.js architecture
def is_nextjs(f):
    return "/chunk_" in f and "/architecture.md" in f
print("Next.js arch:", count_paths(is_nextjs, v3_read_files))

# 52. Picards (3 personas)
def is_persona(f):
    return "Marcus" in f or "Harrison" in f or "David" in f
print("Persona:", count_paths(is_persona, v3_read_files))

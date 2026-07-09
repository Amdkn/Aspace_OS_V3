// 9 cabinets verbatim from Nexus.dc.html cabinetsData
export interface Cabinet {
  name: string;
  icp: string;
  b2: string;
  squads: string[];
  pulse: string;
  status: string;
}

export const cabinets: Cabinet[] = [
  {
    name: "Expert-Comptable",
    icp: "30–50 dossiers / mois",
    b2: "Flash · Reconciliations",
    squads: ["Zero-PII-Facturation", "Reconcile-Bot", "Audit-Log-Immutable"],
    pulse: "94%",
    status: "wave 01 · live",
  },
  {
    name: "Avocat",
    icp: "conflict check + CNIL",
    b2: "Aquaman · AI-Act",
    squads: ["Conflict-Scanner", "Vault-Redactor", "Audit-Log-Immutable"],
    pulse: "91%",
    status: "wave 01 · live",
  },
  {
    name: "Family-Office",
    icp: "> $10M patrimoine",
    b2: "M. Manhunter · Mémoire",
    squads: ["Vault-Redactor", "Sober-Watcher", "Deps-Cleaner"],
    pulse: "97%",
    status: "sanctuary",
  },
  {
    name: "Coach",
    icp: "Notion + Zoom",
    b2: "Cyborg · Workflows",
    squads: ["SOP-Vault", "Mémoire-Sync", "Paperclip-Killer"],
    pulse: "88%",
    status: "queue · wave 02",
  },
  {
    name: "Cabinet-Médical",
    icp: "dossiers patients",
    b2: "Wonder Woman · Zero-PII",
    squads: ["Zero-PII-Remediator", "Health-Vault", "Audit-Log-Immutable"],
    pulse: "96%",
    status: "wave 01",
  },
  {
    name: "Notaire",
    icp: "actes authentiques",
    b2: "Batman · Vault-Audit",
    squads: ["Vault-Redactor", "Conflict-Scanner", "Audit-Log-Immutable"],
    pulse: "90%",
    status: "queue",
  },
  {
    name: "Patrimoine",
    icp: "agrégation multi-actifs",
    b2: "Superman · Migration",
    squads: ["Migrate-Bot", "Reconcile-Bot", "Sober-Watcher"],
    pulse: "92%",
    status: "queue",
  },
  {
    name: "RH",
    icp: "données salariés",
    b2: "Green Lantern · Sober",
    squads: ["Zero-PII-Remediator", "Sober-Watcher", "Deps-Cleaner"],
    pulse: "89%",
    status: "queue",
  },
  {
    name: "Direction",
    icp: "pilotage cabinet",
    b2: "Practice Owner · Routing",
    squads: ["Audit-Log-Immutable", "Sober-Watcher", "Deps-Cleaner"],
    pulse: "99%",
    status: "command",
  },
];

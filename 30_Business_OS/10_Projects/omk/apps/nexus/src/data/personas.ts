// 5 ARIA profiles verbatim from Nexus.dc.html personasData
// Frozen by ADR-ICP-NEXUS-001 — do not rephrase
export interface Persona {
  id: string;
  code: string;
  short: string;
  name: string;
  pain: string;
  remedy: string;
  signal: string;
  lead: string;
  ticket: string;
  accent: string;
  priority: boolean;
}

export const personas: Persona[] = [
  {
    id: "expert-comptable",
    code: "AR/01",
    short: "Expert-Comptable",
    name: "Expert-Comptable",
    pain: "Facturation manuelle multi-dossiers",
    remedy: "Zero-PII Facturation Auto",
    signal: "Pennylane + Excel",
    lead: "30–50 leads / mois",
    ticket: "$750 /mo · self-host",
    accent: "#C8A55C",
    priority: true,
  },
  {
    id: "avocat",
    code: "AR/02",
    short: "Avocat",
    name: "Avocat",
    pain: "Conflict check manuel + CNIL",
    remedy: "AI-Act Conflict Scanner",
    signal: "Dossiers papier + Gmail",
    lead: "conflict, en continu",
    ticket: "$1 500–2 000 /mo",
    accent: "#C49A52",
    priority: false,
  },
  {
    id: "family-office",
    code: "AR/03",
    short: "Family-Office",
    name: "Family-Office",
    pain: "Agrégation Excel multi-patrimoines",
    remedy: "Vault Privé Souverain",
    signal: "> $10M patrimoine",
    lead: "sanctuary, sur invitation",
    ticket: "$5K–50K MRR",
    accent: "#CFB678",
    priority: false,
  },
  {
    id: "coach",
    code: "AR/04",
    short: "Coach",
    name: "Coach",
    pain: "Onboarding client manuel",
    remedy: "SOP Vault Mémoire",
    signal: "Notion + Zoom",
    lead: "queue, wave 02",
    ticket: "$1 000–1 500 /mo",
    accent: "#BE9A5E",
    priority: false,
  },
  {
    id: "cabinet-medical",
    code: "AR/05",
    short: "Cabinet-Médical",
    name: "Cabinet-Médical",
    pain: "Dossiers patients sensibles",
    remedy: "Zero-PII Health Vault",
    signal: "Doctolib + papier",
    lead: "wave 01, conformité",
    ticket: "$1 500–2 000 /mo",
    accent: "#B9A472",
    priority: false,
  },
];

export const defaultPersonaId = "avocat";

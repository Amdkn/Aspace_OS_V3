// 3 Leviers Zero-PII verbatim from Nexus.dc.html leviersData
// Anti-Paperclip lever 02 is structurally applied per ADR-SOBER-002
export interface Levier {
  n: string;
  from: string;
  to: string;
  tag: string;
  body: string;
}

export const leviers: Levier[] = [
  {
    n: "01",
    from: "SaaS public",
    to: "Vault privé",
    tag: "Souveraineté",
    body: "Vos données ne quittent jamais votre périmètre. Pas de SaaS public, pas de tenant partagé. Le vault est à vous.",
  },
  {
    n: "02",
    from: "Greenwashing",
    to: "Conformité-by-default",
    tag: "Zero-PII by design",
    body: "On ne coche pas une case « RGPD ». La redaction Zero-PII est dans le chemin d'exécution. La preuve est l'audit log, pas le badge.",
  },
  {
    n: "03",
    from: "Junior lawyer",
    to: "3 superhumans + 32 squads",
    tag: "Zero-management",
    body: "Vous ne managez personne. Practice Owner route, 8 cabinets exécutent, 32 squads Zero-PII livrent. Vous signez, c'est tout.",
  },
];

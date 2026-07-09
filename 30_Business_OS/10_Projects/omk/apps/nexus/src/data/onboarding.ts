// 3 steps verbatim from Nexus.dc.html renderVals().steps
export interface OnboardingStep {
  n: string;
  title: string;
  body: string;
  meta: string;
}

export const steps: OnboardingStep[] = [
  {
    n: "STEP 01",
    title: "L'audit silencieux",
    body: "Vous droppez une URL. Practice Owner scanne votre stack, détecte les fuites PII, classe le risque AI-Act. Aucun call.",
    meta: "~ 6 min · async",
  },
  {
    n: "STEP 02",
    title: "Le sanctuary",
    body: "Vault privé chiffré provisionné. Audit log immutable activé. Vos données ne sortent jamais du périmètre. Zero-PII by default.",
    meta: "vault chiffré · sovereign",
  },
  {
    n: "STEP 03",
    title: "Activation",
    body: "8 cabinets + 32 squads bootés sur votre mandat. Le vault tourne. Vous signez, ça ships. Sober 1an+ garanti.",
    meta: "live sous 48h",
  },
];

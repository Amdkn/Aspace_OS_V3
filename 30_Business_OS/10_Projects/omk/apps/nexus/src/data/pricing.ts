// 4 tiers USD verbatim from Nexus.dc.html pricing canon
// Frozen by ADR-AAAS-PRICING-001 (5-tier canon, Nexus uses the bottom 4)
export interface PricingTier {
  tier: string;
  price: string;
  note: string;
}

export const pricing: PricingTier[] = [
  { tier: "self-host", price: "$750", note: "Expert-Comptable · /mo" },
  { tier: "pro", price: "$2K", note: "Avocat · Médical · /mo" },
  { tier: "sovereign", price: "$5K", note: "Family-Office · MRR" },
  { tier: "sanctuary", price: "$50K", note: "multi-vault · MRR" },
];

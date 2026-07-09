// SOLARIS — Shared TypeScript interfaces
// Typed domain model for the entire landing page data layer.

export interface SolarisDomain {
  id: string;
  n: string;
  name: string;
  sub: string;
  role: string;
  vp: string;
  squads: string[];
  agents: number;
  status: "active" | "stable" | "vigilant" | "standby";
  metric: string;
  angle: number;
}

export interface AnatomyTier {
  tier: string;
  name: string;
  codename: string;
  role: string;
  desc: string;
  metaphor: string;
  headcount: string;
  members?: string[];
}

export interface ArchetypeTarget {
  k: string;
  v: string;
}

export interface SolarisArchetype {
  id: string;
  code: string;
  name: string;
  fullName: string;
  tag: string;
  glyph: string;
  painName: string;
  painDesc: string;
  remedyName: string;
  remedyDesc: string;
  pitch: string;
  detection: string;
  extractor: string;
  productCode: string;
  ticket?: string;
  targets: ArchetypeTarget[];
  recommended?: boolean;
}

export interface SolarisParadigm {
  n: string;
  name: string;
  promise: string;
  mechanism: string;
  anchor: string;
}

export interface HoldingFiliale {
  id: string;
  code: string;
  name: string;
  scope: string;
  active: boolean;
}

export interface SolarisHolding {
  filiales: HoldingFiliale[];
}

export interface VaultArchData {
  slug: string;
  lead: string;
  headline: string;
  rows: { l: string; s: "high" | "med" | "low"; t: string }[];
  remedy: string;
}

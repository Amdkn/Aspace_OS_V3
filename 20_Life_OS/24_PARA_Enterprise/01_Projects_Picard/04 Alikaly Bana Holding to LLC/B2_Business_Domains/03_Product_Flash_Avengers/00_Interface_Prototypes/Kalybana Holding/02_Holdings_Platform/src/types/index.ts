export interface Holding {
  id: string;
  name: string;
  aum: string;
  role: string;
  description: string;
  iconName: 'Building2' | 'Mountain' | 'Lock';
  isRedacted?: boolean;
}

export interface GlobalMetrics {
  globalExposure: number;
  ytdYield: number;
  lastUpdated: string;
}

export interface SystemStatus {
  version: string;
  build: string;
  latency: string;
  node: string;
}

export interface EngineMetric {
  id: string;
  label: string;
  value: string;
  description: string;
}

export interface EngineModule {
  id: string;
  number: string;
  title: string;
  description: string;
  iconName: 'Database' | 'Network' | 'ShieldCheck';
  badge: string;
}

export interface TeamMember {
  id: string;
  name: string;
  role: string;
  bio: string;
  imageUrl: string;
  primaryFocus: string;
  boardSeats: string[];
}

export interface ContactChannel {
  id: string;
  label: string;
  value: string;
  subtitle: string;
  href: string;
}

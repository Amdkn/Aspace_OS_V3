import type { ReactNode } from 'react';

export type TabKey = 'community' | 'learn' | 'build' | 'brand';

export interface TabDescriptor {
  key: TabKey;
  label: string;
  icon: 'users' | 'graduationCap' | 'wrench' | 'award';
  screen: () => ReactNode;
}

export interface PillarKey {
  key: TabKey;
  icon: 'users' | 'graduationCap' | 'wrench' | 'award';
  accent: string;
}

export interface StatItem {
  n: string;
  l: string;
}

export interface StepItem {
  n: string;
  title: string;
  body: string;
  icon: 'graduationCap' | 'users' | 'sun';
  tex: 'tex-weave' | 'tex-garden' | 'tex-solar';
}

export interface FAQItem {
  q: string;
  a: string;
}

export interface TestimonialQuote {
  quote: string;
  authorName: string;
  authorRole: string;
  initials: string;
  hue: number;
}

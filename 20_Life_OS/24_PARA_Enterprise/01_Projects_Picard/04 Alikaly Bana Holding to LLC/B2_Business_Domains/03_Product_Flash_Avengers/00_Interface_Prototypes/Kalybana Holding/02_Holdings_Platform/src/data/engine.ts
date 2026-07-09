import { EngineMetric, EngineModule } from '../types';

export const engineMetrics: EngineMetric[] = [
  {
    id: 'asset-integrity',
    label: 'Asset Integrity',
    value: '$45M+',
    description: 'Assets recovered through proprietary scanning and automated ledger verification protocols.',
  },
  {
    id: 'scan-velocity',
    label: 'Scan Velocity',
    value: '150+',
    description: 'Properties scanned and indexed daily by the autonomous node network across global jurisdictions.',
  },
];

export const engineModules: EngineModule[] = [
  {
    id: 'ingestion-engine',
    number: '01',
    title: 'Ingestion Engine',
    description: 'Multi-threaded API connectors interfacing with global land registries and digital asset repositories simultaneously.',
    iconName: 'Database',
    badge: 'Supabase Pro Tier',
  },
  {
    id: 'workflow-orchestration',
    number: '02',
    title: 'Workflow Orchestration',
    description: 'Complex conditional logic branching that mirrors the \'n8n\' philosophy—automating legal filings and recovery scripts.',
    iconName: 'Network',
    badge: 'Active Orchestrator',
  },
  {
    id: 'audit-finality',
    number: '03',
    title: 'Audit Finality',
    description: 'Triple-entry accounting verified against decentralized trust layers to ensure 100% recovery accuracy.',
    iconName: 'ShieldCheck',
    badge: 'Verified Ledger',
  },
];

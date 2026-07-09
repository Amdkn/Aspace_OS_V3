// ============================================================================
// Legacy module — kept for backward compatibility while components migrate.
// New code should import Case / Client / Transaction from './supabase/types'
// and fetch via './actions'.
// ============================================================================

export interface Asset {
  id: string;
  name: string;
  type: string;
  description: string;
  aum?: string;
  reserve?: string;
  status: 'ACTIVE' | 'PENDING' | 'REDACTED';
  clearance?: string;
}

/** @deprecated Will be replaced by getActiveCases() in src/lib/actions.ts */
export const MOCK_ASSETS: Asset[] = [
  {
    id: '1',
    name: 'Ali Real Estate Bana LLC',
    type: 'Asset Recovery Specialist',
    description:
      'Specialized in distressed asset recovery and high-frequency liquidation across primary metropolitan corridors.',
    aum: '$12.4M ACTIVE',
    status: 'ACTIVE',
  },
  {
    id: '2',
    name: 'SOB Land Acquisition',
    type: 'Strategic Acquisition',
    description:
      'Aggregating unutilized industrial acreage through automated title verification and debt-stack analysis.',
    reserve: '4,200 AC',
    status: 'ACTIVE',
  },
  {
    id: '3',
    name: '[Redacted]',
    type: 'Confidential Sector',
    description:
      'Proprietary sovereign wealth vehicle. Infrastructure integration and municipal debt management protocols.',
    clearance: 'LEVEL 5 CLEARANCE',
    status: 'REDACTED',
  },
];

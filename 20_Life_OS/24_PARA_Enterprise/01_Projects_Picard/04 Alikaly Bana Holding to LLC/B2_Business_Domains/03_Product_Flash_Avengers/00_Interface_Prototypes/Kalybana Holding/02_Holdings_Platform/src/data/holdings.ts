import { Holding, GlobalMetrics } from '../types';

export const globalMetrics: GlobalMetrics = {
  globalExposure: 248192004.00,
  ytdYield: 14.2,
  lastUpdated: 'T-MINUS 00:14:22',
};

export const holdingsData: Holding[] = [
  {
    id: 'ali-real-estate-bana',
    name: 'Ali Real Estate Bana LLC',
    aum: '$12.4M ACTIVE',
    role: 'Asset Recovery Specialist',
    description: 'Specialized in distressed asset recovery and high-frequency liquidation across primary metropolitan corridors.',
    iconName: 'Building2',
  },
  {
    id: 'sob-land-acquisition',
    name: 'SOB Land Acquisition',
    aum: '4,200 AC RESERVE',
    role: 'Strategic Acquisition',
    description: 'Aggregating unutilized industrial acreage through automated title verification and debt-stack analysis.',
    iconName: 'Mountain',
  },
  {
    id: 'redacted-vehicle',
    name: '[Redacted]',
    aum: 'LEVEL 5 CLEARANCE',
    role: 'Confidential Sector',
    description: 'Proprietary sovereign wealth vehicle. Infrastructure integration and municipal debt management protocols.',
    iconName: 'Lock',
    isRedacted: true,
  },
];

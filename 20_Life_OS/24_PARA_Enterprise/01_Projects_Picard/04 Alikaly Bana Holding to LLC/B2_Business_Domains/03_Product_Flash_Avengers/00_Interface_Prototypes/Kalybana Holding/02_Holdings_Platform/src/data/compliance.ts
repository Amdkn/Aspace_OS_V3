import { TeamMember, ContactChannel } from '../types';

export const teamMembers: TeamMember[] = [
  {
    id: 'kilian-van-der-meer',
    name: 'Kilian Van Der Meer',
    role: 'Managing Partner',
    bio: 'Van Der Meer oversees the strategic deployment of the Kalybana Engine. With twenty years of structural arbitrage experience, his focus remains on the preservation of capital through algorithmic rigidity and ethical governance.',
    imageUrl: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDABrGnwCyWK0YM1h9s0Vz2ZzKhhfm3oLvt4u9c8TKETsOynWLNLzXyPLdoT7pkUI2PXznbBhY8PfGcLSwUL-UqlzsxhMWzljdKA4ZbLD3vq9mHE96ka2AL8RLvICQrswiiB3dGKKowM1Lh7L7BBiKK4kUmhHYnot_RAy7P4eNa8hA23Ik18CqVM6arCiTUS8dYfTGgmd0JXGqSWUgk492Pl1J2NGsHiMTfLZo8QvgElX65BrtqVhUvjIFiVmBSRmtmxfnYFyQPCCOS',
    primaryFocus: 'Sovereign Debt Risk',
    boardSeats: ['Aethelgard', 'Nexus IV'],
  },
];

export const contactChannels: ContactChannel[] = [
  {
    id: 'legal-counsel',
    label: 'Legal Counsel',
    value: 'legal@kalybana.com',
    subtitle: 'PGP: 0x8F22...',
    href: 'mailto:legal@kalybana.com',
  },
  {
    id: 'asset-acquisitions',
    label: 'Asset Acquisitions',
    value: 'acquisitions@kalybana.com',
    subtitle: 'VETTING REQ.',
    href: 'mailto:acquisitions@kalybana.com',
  },
];

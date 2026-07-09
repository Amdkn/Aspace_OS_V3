import type { Metadata } from 'next';
import { BuildHub } from '@/components/HubScreens/BuildHub';
import { IOSDevice } from '@/components/IOSDevice';

export const metadata: Metadata = {
  title: 'Build',
  description:
    "Bâtir ensemble — les outils concrets de la coopérative : contrats, trésorerie, partenaires, jalons.",
};

export default function BuildHubPage() {
  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '24px 12px',
        background: 'var(--bg)',
      }}
    >
      <IOSDevice width={414} height={900} dark>
        <BuildHub />
      </IOSDevice>
    </div>
  );
}

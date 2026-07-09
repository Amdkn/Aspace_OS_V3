import type { Metadata } from 'next';
import { CommunityHub } from '@/components/HubScreens/CommunityHub';
import { IOSDevice } from '@/components/IOSDevice';

export const metadata: Metadata = {
  title: 'Community',
  description:
    "L'Assemblée — discussions, événements et coopératives. Le hub communautaire d'ABC OS.",
};

export default function CommunityPage() {
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
        <CommunityHub />
      </IOSDevice>
    </div>
  );
}

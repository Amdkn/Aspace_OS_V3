import type { Metadata } from 'next';
import { BrandHub } from '@/components/HubScreens/BrandHub';
import { IOSDevice } from '@/components/IOSDevice';

export const metadata: Metadata = {
  title: 'Brand',
  description:
    "Votre identité collective — mesurer la résonance, raconter votre histoire, faire rayonner votre coopérative.",
};

export default function BrandPage() {
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
        <BrandHub />
      </IOSDevice>
    </div>
  );
}

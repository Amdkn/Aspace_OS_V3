import type { Metadata } from 'next';
import { LearnHub } from '@/components/HubScreens/LearnHub';
import { IOSDevice } from '@/components/IOSDevice';

export const metadata: Metadata = {
  title: 'Learn',
  description:
    "Cultiver le savoir — six parcours pour bâtir un sens commun, du principe d'architecte aux principes solarpunk.",
};

export default function LearnPage() {
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
        <LearnHub />
      </IOSDevice>
    </div>
  );
}

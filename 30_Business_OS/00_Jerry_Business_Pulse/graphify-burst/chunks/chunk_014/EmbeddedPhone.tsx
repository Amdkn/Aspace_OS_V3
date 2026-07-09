'use client';

import { useEffect, useState } from 'react';
import { IOSDevice } from './IOSDevice';
import { Icon } from './Icon';
import type { IconName } from './Icon';
import { BrandHub, BuildHub, CommunityHub, LearnHub } from './HubScreens';
import type { TabKey } from '@/lib/types';

const TABS: ReadonlyArray<{ key: TabKey; label: string; icon: IconName }> = [
  { key: 'community', label: 'Community', icon: 'users' },
  { key: 'learn', label: 'Learn', icon: 'graduationCap' },
  { key: 'build', label: 'Build', icon: 'wrench' },
  { key: 'brand', label: 'Brand', icon: 'award' },
];

function Screen({ tab }: { tab: TabKey }) {
  switch (tab) {
    case 'community':
      return <CommunityHub />;
    case 'learn':
      return <LearnHub />;
    case 'build':
      return <BuildHub />;
    case 'brand':
      return <BrandHub />;
    default:
      return null;
  }
}

function EmbeddedNav({
  current,
  onChange,
}: {
  current: TabKey;
  onChange: (k: TabKey) => void;
}) {
  return (
    <div
      style={{
        position: 'absolute',
        left: 12,
        right: 12,
        bottom: 16,
        zIndex: 40,
        height: 68,
        borderRadius: 24,
        background: 'rgba(24,22,20,0.78)',
        backdropFilter: 'blur(20px) saturate(1.4)',
        WebkitBackdropFilter: 'blur(20px) saturate(1.4)',
        border: '1px solid rgba(245,242,235,0.07)',
        boxShadow: '0 18px 40px rgba(0,0,0,0.4), 0 1px 0 rgba(255,255,255,0.04) inset',
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        alignItems: 'center',
        padding: '0 4px',
      }}
    >
      {TABS.map((t) => {
        const active = current === t.key;
        return (
          <button
            key={t.key}
            type="button"
            onClick={() => onChange(t.key)}
            className="h-full flex flex-col items-center justify-center gap-1 relative"
            style={{ color: active ? '#f5f2eb' : '#a89c8a' }}
          >
            {active && (
              <span
                style={{
                  position: 'absolute',
                  top: 6,
                  left: '50%',
                  transform: 'translateX(-50%)',
                  width: 24,
                  height: 3,
                  borderRadius: 3,
                  background: '#e15f41',
                }}
              />
            )}
            <div
              className="flex items-center justify-center"
              style={{
                width: 38,
                height: 32,
                borderRadius: 12,
                background: active ? 'rgba(225,95,65,0.12)' : 'transparent',
                color: active ? '#e15f41' : '#a89c8a',
                transition: 'all .18s',
              }}
            >
              <Icon name={t.icon} size={18} stroke={active ? 2.2 : 1.8} />
            </div>
            <div className="text-[9.5px] font-semibold" style={{ letterSpacing: 0.2 }}>
              {t.label}
            </div>
          </button>
        );
      })}
    </div>
  );
}

export interface EmbeddedPhoneProps {
  tab?: TabKey;
  width?: number;
  height?: number;
  showNav?: boolean;
  interactive?: boolean;
  autoRotate?: boolean;
  onChangeTab?: (k: TabKey) => void;
}

export function EmbeddedPhone({
  tab: initialTab = 'community',
  width = 360,
  height = 760,
  showNav = true,
  interactive = false,
  autoRotate = false,
  onChangeTab,
}: EmbeddedPhoneProps) {
  const [tab, setTab] = useState<TabKey>(initialTab);

  // Keep local state in sync if parent flips the prop
  useEffect(() => {
    setTab(initialTab);
  }, [initialTab]);

  // Hero auto-rotation
  useEffect(() => {
    if (!autoRotate) return;
    const order: TabKey[] = ['community', 'learn', 'build', 'brand'];
    const id = setInterval(() => {
      setTab((cur) => {
        const next = order[(order.indexOf(cur) + 1) % order.length];
        onChangeTab?.(next);
        return next;
      });
    }, 5200);
    return () => clearInterval(id);
  }, [autoRotate, onChangeTab]);

  const handleChange = (k: TabKey) => {
    setTab(k);
    onChangeTab?.(k);
  };

  return (
    <div style={{ width, height, position: 'relative' }}>
      <IOSDevice width={width} height={height} dark hideTabBar>
        <div className="relative h-full" style={{ paddingTop: 54 }}>
          <Screen tab={tab} />
          {showNav && (
            <div
              onClick={interactive ? undefined : (e) => e.stopPropagation()}
              style={{ pointerEvents: interactive ? 'auto' : 'none' }}
            >
              <EmbeddedNav current={tab} onChange={handleChange} />
            </div>
          )}
        </div>
      </IOSDevice>
    </div>
  );
}

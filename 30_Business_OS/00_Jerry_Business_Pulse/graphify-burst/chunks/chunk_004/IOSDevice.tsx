'use client';

import type { ReactNode } from 'react';
import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Icon } from './Icon';
import type { IconName } from './Icon';
import { COLORS } from '@/design/tokens';
import { IOSStatusBar } from './IOSStatusBar';
import { TweaksPanel } from './TweaksPanel';

export interface IOSDeviceProps {
  width?: number;
  height?: number;
  dark?: boolean;
  children?: ReactNode;
  /** When true, hides the bottom tab nav (used for embedded previews on the landing page). */
  hideTabBar?: boolean;
}

interface TabDef {
  key: string;
  label: string;
  icon: IconName;
  href: string;
}

const TABS: TabDef[] = [
  { key: 'community', label: 'Community', icon: 'users', href: '/community' },
  { key: 'learn', label: 'Learn', icon: 'graduationCap', href: '/learn' },
  { key: 'build', label: 'Build', icon: 'wrench', href: '/build-hub' },
  { key: 'brand', label: 'Brand', icon: 'award', href: '/brand' },
];

function BottomTabBar() {
  const pathname = usePathname();
  return (
    <div
      style={{
        position: 'absolute',
        left: 12,
        right: 12,
        bottom: 16,
        zIndex: 40,
        height: 72,
        borderRadius: 28,
        background: 'rgba(24,22,20,0.78)',
        backdropFilter: 'blur(20px) saturate(1.4)',
        WebkitBackdropFilter: 'blur(20px) saturate(1.4)',
        border: '1px solid rgba(245,242,235,0.07)',
        boxShadow:
          '0 18px 40px rgba(0,0,0,0.4), 0 1px 0 rgba(255,255,255,0.04) inset',
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        alignItems: 'center',
        padding: '0 4px',
      }}
    >
      {TABS.map((t) => {
        const active = pathname === t.href;
        return (
          <Link
            key={t.key}
            href={t.href}
            className="h-full flex flex-col items-center justify-center gap-1 relative"
            style={{ color: active ? COLORS.text : COLORS.textMute }}
            aria-current={active ? 'page' : undefined}
          >
            {active && (
              <span
                style={{
                  position: 'absolute',
                  top: 8,
                  left: '50%',
                  transform: 'translateX(-50%)',
                  width: 28,
                  height: 3,
                  borderRadius: 3,
                  background: COLORS.terracotta,
                }}
              />
            )}
            <div
              className="flex items-center justify-center"
              style={{
                width: 44,
                height: 36,
                borderRadius: 14,
                background: active ? 'rgba(225,95,65,0.12)' : 'transparent',
                color: active ? COLORS.terracotta : COLORS.textMute,
                transition: 'all .18s',
              }}
            >
              <Icon name={t.icon} size={20} stroke={active ? 2.2 : 1.8} />
            </div>
            <div
              className="text-[10.5px] font-semibold"
              style={{ letterSpacing: 0.2 }}
            >
              {t.label}
            </div>
          </Link>
        );
      })}
    </div>
  );
}

function TweaksButton({ onClick }: { onClick: () => void }) {
  return (
    <button
      onClick={onClick}
      aria-label="Open tweaks panel"
      className="absolute z-50 flex items-center justify-center"
      style={{
        top: 56,
        right: 12,
        width: 40,
        height: 40,
        borderRadius: 14,
        background: 'rgba(24,22,20,0.78)',
        backdropFilter: 'blur(20px) saturate(1.4)',
        WebkitBackdropFilter: 'blur(20px) saturate(1.4)',
        border: '1px solid rgba(245,242,235,0.07)',
        color: COLORS.text,
        boxShadow: '0 8px 18px rgba(0,0,0,0.4)',
      }}
    >
      <Icon name="sliders" size={17} stroke={1.9} />
    </button>
  );
}

/**
 * iOS 26-style "Liquid Glass" device frame.
 *
 * Faithful port of the legacy `ios-frame.jsx` plus the bottom nav from
 * `app.jsx`. The 4 tabs link to real routes (`/community`, `/learn`,
 * `/build`, `/brand`) via `next/link` so each hub is a real page rather
 * than in-page state. The TweaksPanel is opened from a gear/sliders
 * button anchored to the top-right of the device.
 */
export function IOSDevice({
  width = 414,
  height = 900,
  dark = true,
  children,
  hideTabBar = false,
}: IOSDeviceProps) {
  const [tweaksOpen, setTweaksOpen] = useState(false);
  const bezel = dark ? '#0a0a0a' : '#d8d4cc';
  const ringShadow = dark
    ? '0 40px 60px -20px rgba(0,0,0,0.55), 0 12px 30px -10px rgba(0,0,0,0.4), inset 0 0 0 1.5px rgba(255,255,255,0.06)'
    : '0 30px 50px -20px rgba(0,0,0,0.18), 0 10px 24px -8px rgba(0,0,0,0.12), inset 0 0 0 1.5px rgba(0,0,0,0.06)';

  return (
    <div
      style={{
        position: 'relative',
        width,
        height,
        borderRadius: 48,
        background: bezel,
        boxShadow: ringShadow,
        padding: 12,
        boxSizing: 'border-box',
      }}
    >
      <div
        style={{
          position: 'relative',
          width: '100%',
          height: '100%',
          borderRadius: 36,
          overflow: 'hidden',
          background: dark ? '#0c0b0a' : '#f5f2eb',
          color: dark ? COLORS.text : COLORS.bg,
          fontFamily:
            '-apple-system, system-ui, sans-serif',
          WebkitFontSmoothing: 'antialiased',
        }}
      >
        {/* Dynamic island */}
        <div
          style={{
            position: 'absolute',
            top: 11,
            left: '50%',
            transform: 'translateX(-50%)',
            width: 126,
            height: 37,
            borderRadius: 24,
            background: '#000',
            zIndex: 50,
          }}
        />

        {/* Status bar */}
        <div
          style={{ position: 'absolute', top: 0, left: 0, right: 0, zIndex: 10 }}
        >
          <IOSStatusBar dark={dark} />
        </div>

        {/* Tweaks button */}
        <TweaksButton onClick={() => setTweaksOpen(true)} />

        {/* Children pushed below status bar */}
        <div
          className="relative h-full"
          style={{ paddingTop: 54, boxSizing: 'border-box' }}
        >
          {children}
        </div>

        {/* Bottom tab bar */}
        {!hideTabBar && <BottomTabBar />}

        {/* Home indicator — always on top */}
        <div
          style={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            right: 0,
            zIndex: 60,
            height: 34,
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'flex-end',
            paddingBottom: 8,
            pointerEvents: 'none',
          }}
        >
          <div
            style={{
              width: 139,
              height: 5,
              borderRadius: 100,
              background: dark ? 'rgba(255,255,255,0.7)' : 'rgba(0,0,0,0.25)',
            }}
          />
        </div>
      </div>

      {/* Tweaks drawer (mounts outside the device frame so it can overlay) */}
      <TweaksPanel open={tweaksOpen} onClose={() => setTweaksOpen(false)} />
    </div>
  );
}

export default IOSDevice;

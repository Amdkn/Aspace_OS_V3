'use client';

import type { CSSProperties, ReactNode } from 'react';
import { COLORS } from '@/design/tokens';
import { Icon } from '@/components/Icon';
import type { IconName } from '@/components/Icon';

// ── Small atoms ─────────────────────────────────────────────

export interface AvatarProps {
  initials: string;
  hue?: number;
  size?: number;
  ring?: boolean;
}

export function Avatar({ initials, hue = 30, size = 36, ring = false }: AvatarProps) {
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: '50%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontWeight: 700,
        fontSize: size * 0.36,
        color: '#fff',
        letterSpacing: 0.2,
        background: `radial-gradient(120% 120% at 25% 20%, hsl(${hue} 55% 55%), hsl(${hue + 25} 45% 28%))`,
        boxShadow: ring ? `0 0 0 2px ${COLORS.card}` : 'none',
        flexShrink: 0,
      }}
    >
      {initials}
    </div>
  );
}

export interface PillProps {
  children: ReactNode;
  color?: string;
  bg?: string;
  className?: string;
}

export function Pill({ children, color = COLORS.green, bg, className = '' }: PillProps) {
  return (
    <span
      className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[11px] font-semibold tracking-wide uppercase ${className}`}
      style={{ background: bg || `${color}22`, color }}
    >
      <span
        style={{
          width: 6,
          height: 6,
          borderRadius: 99,
          background: color,
          display: 'inline-block',
        }}
      />
      {children}
    </span>
  );
}

export interface ProgressBarProps {
  value: number;
  color?: string;
  height?: number;
}

export function ProgressBar({ value, color = COLORS.green, height = 6 }: ProgressBarProps) {
  return (
    <div
      style={{
        height,
        background: 'rgba(245,242,235,0.07)',
        borderRadius: 999,
        overflow: 'hidden',
        width: '100%',
      }}
    >
      <div
        style={{
          width: `${value}%`,
          height: '100%',
          background: `linear-gradient(90deg, ${color} 0%, ${color}cc 100%)`,
          borderRadius: 999,
          boxShadow: `0 0 12px ${color}55`,
        }}
      />
    </div>
  );
}

export interface ScreenHeaderProps {
  title: string;
  kicker?: string;
  children?: ReactNode;
}

export function ScreenHeader({ title, kicker, children }: ScreenHeaderProps) {
  return (
    <div className="px-5 pt-3 pb-2">
      {kicker && (
        <div
          className="text-[11px] tracking-[0.18em] uppercase font-semibold mb-1.5"
          style={{ color: COLORS.terracotta }}
        >
          {kicker}
        </div>
      )}
      <h1
        className="text-[28px] leading-[1.05] font-bold"
        style={{ color: COLORS.text, letterSpacing: '-0.02em' }}
      >
        {title}
      </h1>
      {children && <div className="mt-3">{children}</div>}
    </div>
  );
}

export interface SearchBarProps {
  placeholder: string;
  accessory?: ReactNode;
}

export function SearchBar({ placeholder, accessory }: SearchBarProps) {
  return (
    <div className="flex items-center gap-2">
      <div
        className="flex-1 flex items-center gap-2.5 px-3.5 h-11 rounded-2xl"
        style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
      >
        <Icon name="search" size={17} style={{ color: COLORS.textMute }} stroke={2} />
        <input
          placeholder={placeholder}
          className="flex-1 bg-transparent outline-none text-[13.5px]"
          style={{ color: COLORS.text }}
        />
      </div>
      {accessory}
    </div>
  );
}

export function NotifBell() {
  return (
    <button
      className="relative w-11 h-11 rounded-2xl flex items-center justify-center"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        color: COLORS.text,
      }}
    >
      <Icon name="bell" size={19} stroke={1.9} />
      <span
        className="absolute top-2.5 right-2.5 w-2 h-2 rounded-full"
        style={{ background: COLORS.terracotta }}
      />
    </button>
  );
}

export interface CardFrameProps {
  children: ReactNode;
  className?: string;
  style?: CSSProperties;
}

export function CardFrame({ children, className = '', style = {} }: CardFrameProps) {
  return (
    <div
      className={`rounded-3xl ${className}`}
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        ...style,
      }}
    >
      {children}
    </div>
  );
}

// Helper used by the legacy hub components (e.g. SearchBar wraps an Icon)
// exported for completeness in case atoms need typed icon names.
export type HubIconName = IconName;

import type { ReactNode } from 'react';

/**
 * Lucide-style icon set — pure SVG, no external assets.
 *
 * All paths are drawn at 24x24 with stroke-based geometry so a single
 * `Icon` wrapper can render any of them. This replaces the legacy
 * `Object.assign(window, { Icon })` global with a clean ESM export.
 */
export type IconName =
  | 'users'
  | 'graduationCap'
  | 'wrench'
  | 'award'
  | 'store'
  | 'search'
  | 'bell'
  | 'plus'
  | 'heart'
  | 'message'
  | 'share'
  | 'layers'
  | 'megaphone'
  | 'landmark'
  | 'leaf'
  | 'sun'
  | 'bookOpen'
  | 'dollar'
  | 'chevronRight'
  | 'chevronDown'
  | 'arrowRight'
  | 'sparkles'
  | 'sliders'
  | 'bookmark'
  | 'calendar'
  | 'mapPin'
  | 'flame'
  | 'globe'
  | 'trendUp'
  | 'check'
  | 'x'
  | 'arrowLeft'
  | 'send'
  | 'feather';

const ICONS: Record<IconName, ReactNode> = {
  users: (
    <>
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </>
  ),
  graduationCap: (
    <>
      <path d="M22 10 12 5 2 10l10 5 10-5z" />
      <path d="M6 12v5c3 2 9 2 12 0v-5" />
      <path d="M22 10v6" />
    </>
  ),
  wrench: (
    <path d="M14.7 6.3a4.5 4.5 0 0 1 5.95 5.94L15 17.95l-3 3-6-6 3-3 5.7-5.65Z M9 11l-6.5 6.5a1.5 1.5 0 1 0 2 2L11 13" />
  ),
  award: (
    <>
      <circle cx="12" cy="8" r="6" />
      <path d="m8.5 13-1.7 7.2L12 18l5.2 2.2L15.5 13" />
    </>
  ),
  store: (
    <>
      <path d="M3 7l1.5-3h15L21 7" />
      <path d="M3 7v2a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0V7" />
      <path d="M5 10v10h14V10" />
      <path d="M10 20v-5h4v5" />
    </>
  ),
  search: (
    <>
      <circle cx="11" cy="11" r="7" />
      <path d="m20 20-3.5-3.5" />
    </>
  ),
  bell: (
    <>
      <path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8" />
      <path d="M10.3 21a2 2 0 0 0 3.4 0" />
    </>
  ),
  plus: <path d="M12 5v14M5 12h14" />,
  heart: <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z" />,
  message: <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />,
  share: (
    <>
      <circle cx="18" cy="5" r="3" />
      <circle cx="6" cy="12" r="3" />
      <circle cx="18" cy="19" r="3" />
      <path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4" />
    </>
  ),
  layers: (
    <>
      <path d="M12 2 2 7l10 5 10-5-10-5z" />
      <path d="m2 17 10 5 10-5" />
      <path d="m2 12 10 5 10-5" />
    </>
  ),
  megaphone: (
    <>
      <path d="m3 11 18-8v18l-18-8z" />
      <path d="M11.6 16.8a3 3 0 1 1-5.8-1.6" />
    </>
  ),
  landmark: (
    <>
      <path d="M3 22h18" />
      <path d="M5 22V10M9 22V10M15 22V10M19 22V10" />
      <path d="m12 3 9 5H3l9-5z" />
    </>
  ),
  leaf: (
    <>
      <path d="M11 20A7 7 0 0 1 4 13c0-5 4-9 9-9 4 0 7 3 7 7 0 6-5 9-9 9z" />
      <path d="M2 22c4-7 9-10 16-12" />
    </>
  ),
  sun: (
    <>
      <circle cx="12" cy="12" r="4" />
      <path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" />
    </>
  ),
  bookOpen: (
    <>
      <path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z" />
      <path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z" />
    </>
  ),
  dollar: (
    <>
      <path d="M12 2v20" />
      <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
    </>
  ),
  chevronRight: <path d="m9 6 6 6-6 6" />,
  chevronDown: <path d="m6 9 6 6 6-6" />,
  arrowRight: <path d="M5 12h14M13 5l7 7-7 7" />,
  sparkles: (
    <>
      <path d="M12 3 13.6 9 19 10.5 13.6 12 12 18 10.4 12 5 10.5 10.4 9 12 3z" />
      <path d="M19 16l.7 2.3L22 19l-2.3.7L19 22l-.7-2.3L16 19l2.3-.7L19 16z" />
    </>
  ),
  sliders: (
    <>
      <path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3" />
      <path d="M1 14h6M9 8h6M17 16h6" />
    </>
  ),
  bookmark: <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z" />,
  calendar: (
    <>
      <rect x="3" y="4" width="18" height="18" rx="2" />
      <path d="M16 2v4M8 2v4M3 10h18" />
    </>
  ),
  mapPin: (
    <>
      <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 1 1 16 0z" />
      <circle cx="12" cy="10" r="3" />
    </>
  ),
  flame: <path d="M8.5 14.5C6 11.5 8 7 11 4c0 3 4 4 4 8a3 3 0 0 1-3 3M15 14a4 4 0 0 1-3 7c-4 0-7-3-7-7 0-2 1-3 2-4 1 4 5 4 8 4z" />,
  globe: (
    <>
      <circle cx="12" cy="12" r="10" />
      <path d="M2 12h20" />
      <path d="M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20" />
    </>
  ),
  trendUp: <path d="M3 17l6-6 4 4 8-8M14 7h7v7" />,
  check: <path d="m4 12 5 5L20 6" />,
  x: <path d="M6 6l12 12M18 6 6 18" />,
  arrowLeft: <path d="M19 12H5M12 19l-7-7 7-7" />,
  send: <path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z" />,
  feather: (
    <>
      <path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z" />
      <path d="M16 8 2 22" />
      <path d="M17.5 15H9" />
    </>
  ),
};

export interface IconProps {
  name: IconName;
  size?: number;
  stroke?: number;
  className?: string;
  style?: React.CSSProperties;
  fill?: string;
}

export function Icon({
  name,
  size = 20,
  stroke = 1.75,
  className,
  style,
  fill = 'none',
}: IconProps) {
  const path = ICONS[name];
  if (!path) return null;
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill={fill}
      stroke="currentColor"
      strokeWidth={stroke}
      strokeLinecap="round"
      strokeLinejoin="round"
      className={className}
      style={style}
      aria-hidden="true"
    >
      {path}
    </svg>
  );
}

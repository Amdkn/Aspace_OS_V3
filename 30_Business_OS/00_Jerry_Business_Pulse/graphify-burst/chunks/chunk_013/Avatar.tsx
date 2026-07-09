import type { CSSProperties } from 'react';

export interface AvatarProps {
  initials: string;
  hue?: number;
  size?: number;
  ring?: boolean;
  className?: string;
  style?: CSSProperties;
}

export function Avatar({
  initials,
  hue = 30,
  size = 36,
  ring = false,
  className,
  style,
}: AvatarProps) {
  return (
    <div
      className={className}
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
        boxShadow: ring ? '0 0 0 2px #181614' : 'none',
        flexShrink: 0,
        ...style,
      }}
    >
      {initials}
    </div>
  );
}

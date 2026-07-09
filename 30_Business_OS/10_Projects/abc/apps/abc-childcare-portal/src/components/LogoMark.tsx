export interface LogoMarkProps {
  size?: number;
}

export function LogoMark({ size = 28 }: LogoMarkProps) {
  return (
    <svg width={size} height={size} viewBox="0 0 32 32" aria-hidden="true">
      <defs>
        <radialGradient id="lgs" cx="50%" cy="40%" r="55%">
          <stop offset="0%" stopColor="#f6c47a" />
          <stop offset="60%" stopColor="#e15f41" />
          <stop offset="100%" stopColor="#7a2818" />
        </radialGradient>
      </defs>
      {Array.from({ length: 12 }).map((_, i) => {
        const a = (i * Math.PI * 2) / 12;
        const x1 = 16 + Math.cos(a) * 12;
        const y1 = 16 + Math.sin(a) * 12;
        const x2 = 16 + Math.cos(a) * 15.5;
        const y2 = 16 + Math.sin(a) * 15.5;
        return (
          <line
            key={i}
            x1={x1}
            y1={y1}
            x2={x2}
            y2={y2}
            stroke="#e15f41"
            strokeWidth="1.5"
            strokeLinecap="round"
            opacity="0.9"
          />
        );
      })}
      <circle cx="16" cy="16" r="9" fill="url(#lgs)" />
      <path d="M21 12c2-0.5 4 1 3.5 3-2.5 0-4-1-3.5-3z" fill="#10b981" />
    </svg>
  );
}

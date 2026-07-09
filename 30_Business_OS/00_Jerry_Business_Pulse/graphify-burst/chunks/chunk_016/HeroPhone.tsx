'use client';

import { useEffect, useState } from 'react';
import { IOSDevice } from './IOSDevice';
import { CommunityHub } from './HubScreens/CommunityHub';
import { LearnHub } from './HubScreens/LearnHub';
import { BuildHub } from './HubScreens/BuildHub';
import { BrandHub } from './HubScreens/BrandHub';
import { Icon } from './Icon';
import { COLORS } from '@/design/tokens';

const TABS = [
  { key: 'community', label: 'Community', icon: 'users' as const, render: () => <CommunityHub /> },
  { key: 'learn', label: 'Learn', icon: 'graduationCap' as const, render: () => <LearnHub /> },
  { key: 'build', label: 'Build', icon: 'wrench' as const, render: () => <BuildHub /> },
  { key: 'brand', label: 'Brand', icon: 'award' as const, render: () => <BrandHub /> },
];

const ORDER = ['community', 'learn', 'build', 'brand'];

/**
 * Embedded phone preview used on the landing page. Cycles through the 4
 * HUBs every ~5s so visitors can see the OS is real. Mirrors the legacy
 * `landing.jsx` HeroPhone 1:1, plus the floating callouts (Brand Impact
 * 85/100, Solaris Agri-Coop step 3 of 5, 128 new members this week).
 */
export function HeroPhone() {
  const [tab, setTab] = useState('community');

  useEffect(() => {
    const id = window.setInterval(() => {
      setTab((cur) => ORDER[(ORDER.indexOf(cur) + 1) % ORDER.length]);
    }, 5200);
    return () => window.clearInterval(id);
  }, []);

  const T = TABS.find((x) => x.key === tab) ?? TABS[0];

  return (
    <div className="relative">
      {/* Halo */}
      <div
        style={{
          position: 'absolute',
          inset: '-60px -90px',
          zIndex: 0,
          background:
            'radial-gradient(60% 50% at 50% 50%, rgba(225,95,65,0.35), transparent 70%)',
          filter: 'blur(20px)',
        }}
      />
      {/* Phone */}
      <div
        className="relative anim-float"
        style={{ filter: 'drop-shadow(0 50px 80px rgba(0,0,0,0.5))' }}
      >
        <IOSDevice width={368} height={780} dark hideTabBar>
          <div className="relative h-full" style={{ paddingTop: 54 }}>
            {T.render()}
          </div>
        </IOSDevice>
      </div>

      {/* Floating callouts */}
      <div
        className="absolute hidden lg:flex flex-col gap-1.5 px-3.5 py-2.5 rounded-2xl text-left"
        style={{
          left: -180,
          top: 90,
          width: 200,
          background: 'rgba(24,22,20,0.85)',
          border: '1px solid var(--line)',
          backdropFilter: 'blur(8px)',
          zIndex: 10,
          color: COLORS.text,
        }}
      >
        <div className="eyebrow" style={{ fontSize: 9 }}>
          Brand Impact
        </div>
        <div className="flex items-baseline gap-1">
          <span className="font-serif italic text-[36px] leading-none">85</span>
          <span
            className="text-[12px] font-semibold"
            style={{ color: COLORS.textMute }}
          >
            / 100
          </span>
        </div>
        <div className="text-[11px]" style={{ color: COLORS.textMute }}>
          Résonance communautaire —{' '}
          <span style={{ color: COLORS.green }}>+6 cette semaine</span>
        </div>
        {/* connector */}
        <svg
          width="140"
          height="30"
          style={{ position: 'absolute', right: -130, top: 34 }}
        >
          <path
            d="M2 15 Q70 15 130 18"
            stroke="rgba(245,242,235,0.18)"
            strokeDasharray="3 4"
            fill="none"
          />
          <circle cx="130" cy="18" r={3} fill={COLORS.terracotta} />
        </svg>
      </div>

      <div
        className="absolute hidden lg:flex items-center gap-2.5 px-3.5 py-2 rounded-2xl"
        style={{
          right: -170,
          top: 360,
          background: 'rgba(24,22,20,0.85)',
          border: '1px solid var(--line)',
          backdropFilter: 'blur(8px)',
          zIndex: 10,
          color: COLORS.text,
        }}
      >
        <span
          className="anim-pulse-dot"
          style={{
            width: 8,
            height: 8,
            borderRadius: 99,
            background: COLORS.green,
            boxShadow: `0 0 12px ${COLORS.green}`,
          }}
        />
        <div>
          <div className="text-[11px]" style={{ color: COLORS.textMute }}>
            Solaris Agri-Coop
          </div>
          <div className="text-[12.5px] font-semibold">
            Étape 3 de 5 · validée
          </div>
        </div>
        <svg
          width="140"
          height="30"
          style={{ position: 'absolute', left: -130, top: 14 }}
        >
          <path
            d="M138 15 Q70 15 10 18"
            stroke="rgba(245,242,235,0.18)"
            strokeDasharray="3 4"
            fill="none"
          />
          <circle cx={10} cy={18} r={3} fill={COLORS.green} />
        </svg>
      </div>

      <div
        className="absolute hidden lg:flex items-center gap-3 px-3.5 py-2.5 rounded-2xl"
        style={{
          left: -220,
          bottom: 120,
          width: 230,
          background: 'rgba(24,22,20,0.85)',
          border: '1px solid var(--line)',
          backdropFilter: 'blur(8px)',
          zIndex: 10,
          color: COLORS.text,
        }}
      >
        <div
          className="w-9 h-9 rounded-xl flex items-center justify-center"
          style={{
            background: 'rgba(225,95,65,0.18)',
            color: COLORS.terracotta,
          }}
        >
          <Icon name="users" size={18} />
        </div>
        <div className="flex-1">
          <div className="text-[12.5px] font-semibold">128 nouveaux membres</div>
          <div className="text-[11px]" style={{ color: COLORS.textMute }}>
            cette semaine, 9 pays
          </div>
        </div>
        <svg
          width="140"
          height="30"
          style={{ position: 'absolute', right: -130, top: 18 }}
        >
          <path
            d="M2 15 Q70 5 130 8"
            stroke="rgba(245,242,235,0.18)"
            strokeDasharray="3 4"
            fill="none"
          />
          <circle cx={130} cy={8} r={3} fill={COLORS.terracotta} />
        </svg>
      </div>
    </div>
  );
}

export default HeroPhone;

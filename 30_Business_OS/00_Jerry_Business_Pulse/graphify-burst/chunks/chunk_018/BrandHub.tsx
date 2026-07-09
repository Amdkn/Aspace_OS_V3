'use client';

import { COLORS } from '@/design/tokens';
import { Icon } from '@/components/Icon';
import type { IconName } from '@/components/Icon';
import { Pill, ScreenHeader } from './atoms';

// ── RadialScore (the signature 85/100 ring) ────────────────

interface RadialScoreProps {
  value?: number;
  max?: number;
}

function RadialScore({ value = 85, max = 100 }: RadialScoreProps) {
  const r = 78;
  const circ = 2 * Math.PI * r;
  const off = circ * (1 - value / max);
  return (
    <div className="relative" style={{ width: 200, height: 200 }}>
      <svg width="200" height="200" viewBox="0 0 200 200">
        <defs>
          <linearGradient id="scoreG" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="#10b981" />
            <stop offset="60%" stopColor="#34d3a1" />
            <stop offset="100%" stopColor="#e15f41" />
          </linearGradient>
        </defs>
        {/* track */}
        <circle
          cx="100"
          cy="100"
          r={r}
          stroke="rgba(245,242,235,0.07)"
          strokeWidth="14"
          fill="none"
        />
        {/* tick marks */}
        {Array.from({ length: 60 }).map((_, i) => {
          const a = (i / 60) * Math.PI * 2 - Math.PI / 2;
          const x1 = 100 + Math.cos(a) * 92;
          const y1 = 100 + Math.sin(a) * 92;
          const x2 = 100 + Math.cos(a) * 96;
          const y2 = 100 + Math.sin(a) * 96;
          return (
            <line
              key={i}
              x1={x1}
              y1={y1}
              x2={x2}
              y2={y2}
              stroke="rgba(245,242,235,0.12)"
              strokeWidth={i % 5 === 0 ? 1.5 : 1}
            />
          );
        })}
        {/* progress */}
        <circle
          cx="100"
          cy="100"
          r={r}
          stroke="url(#scoreG)"
          strokeWidth="14"
          fill="none"
          strokeLinecap="round"
          strokeDasharray={circ}
          strokeDashoffset={off}
          transform="rotate(-90 100 100)"
          style={{ filter: 'drop-shadow(0 0 12px rgba(16,185,129,0.35))' }}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <div
          className="text-[11px] tracking-[0.22em] uppercase font-semibold"
          style={{ color: COLORS.textDim }}
        >
          Brand Impact
        </div>
        <div className="flex items-baseline mt-1">
          <span
            className="font-serif italic text-[64px] leading-none"
            style={{ color: COLORS.text }}
          >
            85
          </span>
          <span
            className="text-[15px] font-semibold ml-1"
            style={{ color: COLORS.textMute }}
          >
            / 100
          </span>
        </div>
        <div
          className="text-[10.5px] uppercase tracking-[0.18em] font-semibold mt-1"
          style={{ color: COLORS.green }}
        >
          ↗ +6 this week
        </div>
      </div>
    </div>
  );
}

// ── ActionRow ──────────────────────────────────────────────

interface ActionRowProps {
  icon: IconName;
  title: string;
  sub: string;
  accent: string;
  last?: boolean;
}

function ActionRow({ icon, title, sub, accent, last }: ActionRowProps) {
  return (
    <button
      className="w-full flex items-center gap-3.5 px-4 py-3.5 text-left"
      style={{ borderBottom: last ? 'none' : `1px solid ${COLORS.line}` }}
    >
      <div
        className="w-11 h-11 rounded-2xl flex items-center justify-center flex-shrink-0"
        style={{ background: `${accent}1c`, color: accent }}
      >
        <Icon name={icon} size={20} />
      </div>
      <div className="flex-1 min-w-0">
        <div className="text-[14.5px] font-semibold" style={{ color: COLORS.text }}>
          {title}
        </div>
        <div className="text-[12px] mt-0.5" style={{ color: COLORS.textMute }}>
          {sub}
        </div>
      </div>
      <Icon name="chevronRight" size={18} style={{ color: COLORS.textDim }} />
    </button>
  );
}

// ── BrandHub ───────────────────────────────────────────────

export function BrandHub() {
  return (
    <div
      className="abc-screen relative h-full flex flex-col"
      style={{ background: COLORS.bg, color: COLORS.text }}
    >
      <ScreenHeader title="Brand Hub" kicker="Votre identité collective" />

      <div className="flex-1 overflow-y-auto px-5 pb-28 scrollbar-hide">
        {/* Score */}
        <div
          className="rounded-3xl flex flex-col items-center pt-5 pb-5 px-4 mt-2 relative overflow-hidden"
          style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
        >
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background:
                'radial-gradient(280px 200px at 50% -10%, rgba(16,185,129,0.16), transparent 70%)',
              pointerEvents: 'none',
            }}
          />
          <RadialScore value={85} />
          <div
            className="text-[12.5px] mt-2 text-center max-w-[260px]"
            style={{ color: COLORS.textMute }}
          >
            Your current community resonance. Steady growth this month — keep
            telling your story.
          </div>

          <div className="grid grid-cols-3 gap-2 mt-4 w-full">
            {[
              { l: 'Story', v: '92' },
              { l: 'Reach', v: '78' },
              { l: 'Impact', v: '84' },
            ].map((s) => (
              <div
                key={s.l}
                className="rounded-2xl px-3 py-2.5"
                style={{ background: COLORS.bgAlt, border: `1px solid ${COLORS.line}` }}
              >
                <div
                  className="text-[10.5px] tracking-[0.16em] uppercase font-semibold"
                  style={{ color: COLORS.textDim }}
                >
                  {s.l}
                </div>
                <div
                  className="text-[20px] font-bold mt-0.5"
                  style={{ color: COLORS.text }}
                >
                  {s.v}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Action list */}
        <div
          className="mt-5 rounded-3xl overflow-hidden"
          style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
        >
          <ActionRow
            icon="bookOpen"
            title="Crafting Your Story"
            sub="Define values, mission, and visual identity."
            accent={COLORS.terracotta}
          />
          <ActionRow
            icon="dollar"
            title="Monetization Strategies"
            sub="Explore pricing, digital products, and grants."
            accent="#d4b042"
          />
          <ActionRow
            icon="users"
            title="Community Impact"
            sub="Track social good and member collaboration."
            accent={COLORS.green}
            last
          />
        </div>

        {/* Inspiration */}
        <section className="mt-6">
          <div className="flex items-center justify-between mb-2.5">
            <h2 className="text-[16px] font-bold">Inspiration Hub</h2>
            <Icon name="flame" size={16} style={{ color: COLORS.terracotta }} />
          </div>
          <article
            className="rounded-3xl overflow-hidden flex"
            style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
          >
            <div className="relative flex-shrink-0" style={{ width: 124 }}>
              <div className="tex-loom" style={{ position: 'absolute', inset: 0 }} />
              <div
                style={{
                  position: 'absolute',
                  inset: 0,
                  background:
                    'linear-gradient(90deg, transparent 60%, rgba(34,31,28,0.85) 100%)',
                }}
              />
              <div className="absolute top-2.5 left-2.5">
                <Pill color="#fff" bg="rgba(0,0,0,0.4)">
                  Case study
                </Pill>
              </div>
            </div>
            <div className="p-3.5 flex-1">
              <div
                className="text-[10.5px] tracking-[0.18em] uppercase font-semibold"
                style={{ color: COLORS.terracotta }}
              >
                Soko Weavers
              </div>
              <div
                className="text-[14px] font-bold leading-[1.2] mt-1"
                style={{ color: COLORS.text }}
              >
                Doubled Their Reach
              </div>
              <div
                className="text-[11.5px] mt-1.5 leading-[1.4]"
                style={{ color: COLORS.textMute }}
              >
                How cooperative marketing expanded their global footprint.
              </div>
              <div
                className="flex items-center gap-1.5 mt-2 text-[11.5px] font-semibold"
                style={{ color: COLORS.green }}
              >
                Read story <Icon name="arrowRight" size={13} />
              </div>
            </div>
          </article>

          <article
            className="rounded-3xl flex items-center gap-3 px-4 py-3 mt-3"
            style={{ background: COLORS.card, border: `1px solid ${COLORS.line}` }}
          >
            <div
              className="w-11 h-11 rounded-2xl flex items-center justify-center"
              style={{ background: `${COLORS.green}1f`, color: COLORS.green }}
            >
              <Icon name="globe" size={20} />
            </div>
            <div className="flex-1 min-w-0">
              <div
                className="text-[13.5px] font-semibold"
                style={{ color: COLORS.text }}
              >
                Brand Atlas
              </div>
              <div className="text-[11.5px]" style={{ color: COLORS.textMute }}>
                Visual identities from 24 African co-ops
              </div>
            </div>
            <Icon name="chevronRight" size={18} style={{ color: COLORS.textDim }} />
          </article>
        </section>
      </div>
    </div>
  );
}

export default BrandHub;

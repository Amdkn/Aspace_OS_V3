'use client';

import { useState } from 'react';
import { COLORS } from '@/design/tokens';
import { Icon } from '@/components/Icon';
import {
  Avatar,
  CardFrame,
  NotifBell,
  Pill,
  ScreenHeader,
  SearchBar,
} from './atoms';

// ── FeedCard ────────────────────────────────────────────────

interface FeedCardProps {
  name: string;
  initials: string;
  hue: number;
  time: string;
  badge?: string;
  text: React.ReactNode;
  likes: number;
  comments: number;
  shares?: number;
  image?: string;
  last?: boolean;
}

function FeedCard({
  name,
  initials,
  hue,
  time,
  badge,
  text,
  likes,
  comments,
  shares,
  image,
  last,
}: FeedCardProps) {
  return (
    <article
      className="anim-fade-up"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        borderRadius: 24,
        padding: 16,
        marginBottom: last ? 0 : 14,
      }}
    >
      <header className="flex items-center gap-3">
        <Avatar initials={initials} hue={hue} size={42} />
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2">
            <div
              className="text-[14.5px] font-semibold truncate"
              style={{ color: COLORS.text }}
            >
              {name}
            </div>
            {badge && (
              <span
                className="text-[10px] px-1.5 py-0.5 rounded-md font-semibold tracking-wide"
                style={{ background: `${COLORS.green}22`, color: COLORS.green }}
              >
                {badge}
              </span>
            )}
          </div>
          <div className="text-[11.5px]" style={{ color: COLORS.textMute }}>
            {time}
          </div>
        </div>
        <button
          className="w-8 h-8 rounded-full flex items-center justify-center"
          style={{ color: COLORS.textMute }}
        >
          <svg width="16" height="4" viewBox="0 0 16 4">
            <circle cx="2" cy="2" r="1.6" fill="currentColor" />
            <circle cx="8" cy="2" r="1.6" fill="currentColor" />
            <circle cx="14" cy="2" r="1.6" fill="currentColor" />
          </svg>
        </button>
      </header>

      <p className="text-[14px] leading-[1.5] mt-3" style={{ color: COLORS.text }}>
        {text}
      </p>

      {image && (
        <div
          className={`mt-3 rounded-2xl overflow-hidden relative ${image}`}
          style={{ height: 168, border: `1px solid ${COLORS.line}` }}
        >
          <div
            style={{
              position: 'absolute',
              inset: 0,
              background: 'linear-gradient(180deg, transparent 50%, rgba(0,0,0,0.55) 100%)',
            }}
          />
          <div className="absolute bottom-3 left-3 right-3 flex items-end justify-between">
            <div>
              <div
                className="text-[11px] uppercase tracking-[0.18em] font-semibold"
                style={{ color: '#cdebd6' }}
              >
                Solaris Agri-Coop · Kenya
              </div>
              <div className="text-[15px] font-semibold text-white">
                Maïs &amp; sorgho · Saison 2
              </div>
            </div>
            <Pill color="#cdebd6">harvest</Pill>
          </div>
        </div>
      )}

      <footer
        className="flex items-center gap-5 mt-3.5 pt-3.5"
        style={{ borderTop: `1px solid ${COLORS.line}` }}
      >
        <button
          className="flex items-center gap-1.5 text-[12.5px] font-medium"
          style={{ color: COLORS.textMute }}
        >
          <Icon name="heart" size={16} stroke={1.7} /> {likes}
        </button>
        <button
          className="flex items-center gap-1.5 text-[12.5px] font-medium"
          style={{ color: COLORS.textMute }}
        >
          <Icon name="message" size={16} stroke={1.7} /> {comments}
        </button>
        {shares !== undefined && (
          <button
            className="flex items-center gap-1.5 text-[12.5px] font-medium"
            style={{ color: COLORS.textMute }}
          >
            <Icon name="share" size={15} stroke={1.7} /> {shares}
          </button>
        )}
        <div className="flex-1" />
        <button style={{ color: COLORS.textMute }}>
          <Icon name="bookmark" size={16} stroke={1.7} />
        </button>
      </footer>
    </article>
  );
}

// ── CommunityHub ───────────────────────────────────────────

export function CommunityHub() {
  const [sub, setSub] = useState('Feed');
  return (
    <div
      className="abc-screen relative h-full flex flex-col"
      style={{ background: COLORS.bg, color: COLORS.text }}
    >
      <ScreenHeader title="Community" kicker="L'Assemblée">
        <SearchBar
          placeholder="Search discussions and members…"
          accessory={<NotifBell />}
        />
        <div
          className="flex items-center gap-5 mt-4 px-1 text-[14px] font-semibold"
          style={{ color: COLORS.textMute }}
        >
          {['Feed', 'Co-ops', 'Events'].map((t) => (
            <button
              key={t}
              onClick={() => setSub(t)}
              className={`tab-underline ${sub === t ? 'active' : ''}`}
              style={{
                color: sub === t ? COLORS.text : COLORS.textMute,
                paddingBottom: 2,
              }}
            >
              {t}
              {t === 'Events' && (
                <span
                  className="ml-1.5 text-[10px] px-1.5 py-[1px] rounded-full font-bold"
                  style={{ background: COLORS.terracotta, color: '#fff' }}
                >
                  3
                </span>
              )}
            </button>
          ))}
        </div>
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto px-5 pt-3 pb-28 scrollbar-hide">
        <FeedCard
          name="Kaelan Patel"
          initials="KP"
          hue={210}
          time="2h ago · Lagos, NG"
          text={
            <>
              Looking for advice from anyone who has gone through the process.
              What are the key documents and registrations required?{' '}
              <span style={{ color: COLORS.terracotta, fontWeight: 600 }}>#Legal</span>{' '}
              <span style={{ color: COLORS.terracotta, fontWeight: 600 }}>#Startup</span>
            </>
          }
          likes={12}
          comments={5}
          shares={2}
        />
        <FeedCard
          name="Amara Okoro"
          initials="AO"
          hue={28}
          badge="Co-op lead"
          time="1 day ago · Nairobi, KE"
          text={
            <>
              Our Agri-Tech coop just secured its first round of funding! A huge
              thank you to everyone in the{' '}
              <span style={{ color: COLORS.green, fontWeight: 600 }}>#BuildHub</span>{' '}
              for the feedback on our pitch deck. The journey continues 🌱
            </>
          }
          image="tex-field"
          likes={78}
          comments={23}
          last
        />

        <div
          className="mt-3 mb-1 text-[11px] tracking-[0.18em] uppercase font-semibold px-1"
          style={{ color: COLORS.textDim }}
        >
          Suggested for you
        </div>
        <CardFrame className="px-4 py-3 flex items-center gap-3">
          <div
            className="w-11 h-11 rounded-2xl flex items-center justify-center"
            style={{ background: `${COLORS.green}22`, color: COLORS.green }}
          >
            <Icon name="users" size={20} />
          </div>
          <div className="flex-1 min-w-0">
            <div className="text-[14px] font-semibold">Sahel Solar Builders</div>
            <div className="text-[12px]" style={{ color: COLORS.textMute }}>
              248 members · 4 you know
            </div>
          </div>
          <button
            className="px-3.5 h-9 rounded-full text-[12.5px] font-semibold"
            style={{ background: COLORS.terracotta, color: '#fff' }}
          >
            Join
          </button>
        </CardFrame>
      </div>

      {/* FAB */}
      <button
        className="absolute right-5 bottom-[112px] w-14 h-14 rounded-full flex items-center justify-center"
        style={{
          background: `linear-gradient(180deg, ${COLORS.terracotta}, ${COLORS.terracottaDeep})`,
          color: '#fff',
          boxShadow:
            '0 14px 30px -8px rgba(225,95,65,0.6), 0 2px 0 rgba(255,255,255,0.15) inset',
        }}
      >
        <Icon name="plus" size={26} stroke={2.3} />
      </button>
    </div>
  );
}

export default CommunityHub;

'use client';

import { useState } from 'react';
import { COLORS } from '@/design/tokens';
import { Icon } from '@/components/Icon';
import type { IconName } from '@/components/Icon';
import {
  Avatar,
  Pill,
  ProgressBar,
  ScreenHeader,
} from './atoms';

// ── ProjectCard ────────────────────────────────────────────

interface ProjectCardMember {
  i: string;
  h: number;
}

interface ProjectCardProps {
  name: string;
  tagline: string;
  tex: string;
  status: string;
  statusColor: string;
  milestoneText: string;
  milestoneCurrent: number;
  milestoneTotal: number;
  next: string;
  members: ProjectCardMember[];
}

function ProjectCard({
  name,
  tagline,
  tex,
  status,
  statusColor,
  milestoneText,
  milestoneCurrent,
  milestoneTotal,
  next,
  members,
}: ProjectCardProps) {
  const progress = (milestoneCurrent / milestoneTotal) * 100;
  return (
    <article
      className="rounded-3xl overflow-hidden anim-fade-up"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        marginBottom: 14,
      }}
    >
      <div className="relative" style={{ height: 152 }}>
        <div className={tex} style={{ position: 'absolute', inset: 0 }} />
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: 'linear-gradient(180deg, rgba(0,0,0,0.05) 40%, rgba(0,0,0,0.6) 100%)',
          }}
        />
        <div className="absolute top-3 left-3 right-3 flex items-start justify-between">
          <Pill color={statusColor}>{status}</Pill>
          <button
            className="w-8 h-8 rounded-full flex items-center justify-center"
            style={{
              background: 'rgba(0,0,0,0.35)',
              backdropFilter: 'blur(6px)',
              color: '#fff',
            }}
          >
            <Icon name="chevronRight" size={16} />
          </button>
        </div>
        <div className="absolute bottom-3 left-4 right-4">
          <div className="text-[18px] font-bold leading-tight" style={{ color: '#fff' }}>
            {name}
          </div>
          <div className="text-[12px] opacity-85 mt-0.5" style={{ color: '#fff' }}>
            {tagline}
          </div>
        </div>
      </div>

      <div className="p-4">
        <div className="flex items-center justify-between mb-2">
          <div className="text-[12px] font-semibold" style={{ color: COLORS.textMute }}>
            {milestoneText}
          </div>
          <div className="text-[12px] font-bold" style={{ color: statusColor }}>
            {milestoneCurrent} / {milestoneTotal}
          </div>
        </div>
        <ProgressBar value={progress} color={statusColor} height={6} />

        <div className="mt-3.5 flex items-center justify-between">
          <div className="flex items-center gap-2 min-w-0">
            <div
              className="w-7 h-7 rounded-lg flex-shrink-0 flex items-center justify-center"
              style={{ background: `${statusColor}1f`, color: statusColor }}
            >
              <Icon name="arrowRight" size={14} />
            </div>
            <div className="min-w-0">
              <div
                className="text-[10.5px] uppercase tracking-[0.16em] font-semibold"
                style={{ color: COLORS.textDim }}
              >
                Next
              </div>
              <div
                className="text-[13px] font-semibold truncate"
                style={{ color: COLORS.text }}
              >
                {next}
              </div>
            </div>
          </div>

          {/* Avatars */}
          <div className="flex items-center -space-x-2">
            {members.map((m, i) => (
              <div key={i} style={{ zIndex: members.length - i }}>
                <Avatar initials={m.i} hue={m.h} size={30} ring />
              </div>
            ))}
            <div
              className="w-[30px] h-[30px] rounded-full flex items-center justify-center text-[11px] font-bold"
              style={{
                background: COLORS.cardHi,
                color: COLORS.text,
                boxShadow: `0 0 0 2px ${COLORS.card}`,
                zIndex: 0,
              }}
            >
              +2
            </div>
          </div>
        </div>
      </div>
    </article>
  );
}

// ── ToolTile ───────────────────────────────────────────────

interface ToolTileProps {
  icon: IconName;
  title: string;
  sub: string;
  accent: string;
}

function ToolTile({ icon, title, sub, accent }: ToolTileProps) {
  return (
    <button
      className="rounded-2xl p-3.5 text-left flex flex-col gap-3"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        minHeight: 124,
      }}
    >
      <div
        className="w-10 h-10 rounded-xl flex items-center justify-center"
        style={{ background: `${accent}1f`, color: accent }}
      >
        <Icon name={icon} size={20} />
      </div>
      <div>
        <div className="text-[13.5px] font-semibold leading-tight">{title}</div>
        <div className="text-[11px] mt-1" style={{ color: COLORS.textMute }}>
          {sub}
        </div>
      </div>
    </button>
  );
}

// ── BuildHub ───────────────────────────────────────────────

export function BuildHub() {
  const [tab, setTab] = useState('My Projects');

  return (
    <div
      className="abc-screen relative h-full flex flex-col"
      style={{ background: COLORS.bg, color: COLORS.text }}
    >
      <ScreenHeader title="Build Hub" kicker="Bâtir ensemble">
        <div
          className="flex gap-2 p-1 rounded-2xl"
          style={{
            background: COLORS.card,
            border: `1px solid ${COLORS.line}`,
            width: '100%',
          }}
        >
          {['My Projects', 'Cooperative Tools'].map((t) => (
            <button
              key={t}
              onClick={() => setTab(t)}
              className="flex-1 h-10 text-[13px] font-semibold rounded-xl transition-colors"
              style={{
                background: tab === t ? COLORS.terracotta : 'transparent',
                color: tab === t ? '#fff' : COLORS.textMute,
              }}
            >
              {t}
            </button>
          ))}
        </div>
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto px-5 pt-3 pb-28 scrollbar-hide">
        {tab === 'My Projects' ? (
          <>
            <ProjectCard
              name="Solaris Agri-Coop"
              tagline="Solar-powered cooperative farming · Kenya"
              tex="tex-solar"
              status="In Progress"
              statusColor={COLORS.green}
              milestoneText="Milestone progress"
              milestoneCurrent={3}
              milestoneTotal={5}
              next="Finalize Distribution Plan"
              members={[
                { i: 'AO', h: 28 },
                { i: 'KP', h: 210 },
                { i: 'JM', h: 140 },
              ]}
            />
            <ProjectCard
              name="Umoja Weavers Collective"
              tagline="Heritage textiles & shared looms · Tanzania"
              tex="tex-garden"
              status="Planning"
              statusColor={COLORS.blue}
              milestoneText="Milestone progress"
              milestoneCurrent={1}
              milestoneTotal={8}
              next="Draft Cooperative Agreement"
              members={[
                { i: 'NN', h: 320 },
                { i: 'TM', h: 18 },
                { i: 'EA', h: 280 },
              ]}
            />

            {/* CTA — dotted */}
            <button
              className="w-full rounded-3xl px-5 py-6 flex flex-col items-center text-center mt-1"
              style={{
                border: `1.5px dashed ${COLORS.line}`,
                background:
                  'linear-gradient(180deg, rgba(225,95,65,0.05) 0%, rgba(225,95,65,0.0) 100%)',
              }}
            >
              <div
                className="w-12 h-12 rounded-full flex items-center justify-center"
                style={{ background: `${COLORS.terracotta}22`, color: COLORS.terracotta }}
              >
                <Icon name="plus" size={22} stroke={2.2} />
              </div>
              <div
                className="text-[14.5px] font-semibold mt-2.5"
                style={{ color: COLORS.text }}
              >
                Ready to build together?
              </div>
              <div
                className="text-[12.5px] leading-[1.45] mt-1.5 max-w-[260px]"
                style={{ color: COLORS.textMute }}
              >
                Tap the "+" button to start your first cooperative business and
                bring your vision to life.
              </div>
            </button>
          </>
        ) : (
          <div className="grid grid-cols-2 gap-3">
            <ToolTile
              icon="feather"
              title="Agreement Drafter"
              sub="Co-op contract templates"
              accent={COLORS.green}
            />
            <ToolTile
              icon="dollar"
              title="Treasury Ledger"
              sub="Shared books & payouts"
              accent={COLORS.terracotta}
            />
            <ToolTile
              icon="users"
              title="Member Onboarding"
              sub="Vote, invite, ratify"
              accent="#d4b042"
            />
            <ToolTile
              icon="globe"
              title="Supply Network"
              sub="Find regional partners"
              accent={COLORS.green}
            />
            <ToolTile
              icon="calendar"
              title="Harvest Calendar"
              sub="Seasonal milestones"
              accent="#5a9f6c"
            />
            <ToolTile
              icon="trendUp"
              title="Impact Reporting"
              sub="Track regenerative KPIs"
              accent={COLORS.terracotta}
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default BuildHub;

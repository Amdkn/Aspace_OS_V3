'use client';

import { COLORS } from '@/design/tokens';
import { Icon } from '@/components/Icon';
import type { IconName } from '@/components/Icon';
import {
  Pill,
  ProgressBar,
  ScreenHeader,
  SearchBar,
} from './atoms';

// ── CourseCard ─────────────────────────────────────────────

interface CourseCardProps {
  title: string;
  sub: string;
  progress: number;
  color: IconName;
  accent: string;
}

function CourseCard({ title, sub, progress, color, accent }: CourseCardProps) {
  return (
    <div
      className="flex-shrink-0 rounded-3xl p-4 flex flex-col justify-between"
      style={{
        width: 200,
        height: 168,
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
      }}
    >
      <div
        className="w-10 h-10 rounded-xl flex items-center justify-center"
        style={{ background: `${accent}22`, color: accent }}
      >
        <Icon name={color} size={20} />
      </div>
      <div>
        <div
          className="text-[10.5px] tracking-[0.18em] uppercase font-semibold mb-1"
          style={{ color: COLORS.textDim }}
        >
          {sub}
        </div>
        <div
          className="text-[15.5px] font-semibold leading-[1.2] mb-2.5"
          style={{ color: COLORS.text }}
        >
          {title}
        </div>
        <div className="flex items-center gap-2">
          <ProgressBar value={progress} color={accent} height={5} />
          <span
            className="text-[11px] font-semibold"
            style={{ color: accent }}
          >
            {progress}%
          </span>
        </div>
      </div>
    </div>
  );
}

// ── RecCard ────────────────────────────────────────────────

interface RecCardProps {
  title: string;
  sub: string;
  tex: string;
  badge: string;
}

function RecCard({ title, sub, tex, badge }: RecCardProps) {
  return (
    <div
      className="rounded-3xl relative overflow-hidden flex-shrink-0"
      style={{
        width: 220,
        height: 248,
        border: `1px solid ${COLORS.line}`,
      }}
    >
      <div className={tex} style={{ position: 'absolute', inset: 0 }} />
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background:
            'linear-gradient(180deg, rgba(0,0,0,0.05) 35%, rgba(8,6,4,0.9) 100%)',
        }}
      />
      <div className="absolute top-3 left-3">
        <Pill color="#f5f2eb" bg="rgba(0,0,0,0.4)">
          {badge}
        </Pill>
      </div>
      <div className="absolute bottom-4 left-4 right-4">
        <div
          className="text-[11px] tracking-[0.18em] uppercase font-semibold opacity-80"
          style={{ color: '#fff' }}
        >
          {sub}
        </div>
        <div
          className="text-[18px] font-bold mt-1 leading-[1.15]"
          style={{ color: '#fff' }}
        >
          {title}
        </div>
        <div
          className="text-[12px] mt-1.5 opacity-80"
          style={{ color: '#fff' }}
        >
          8 lessons · 2h 40m
        </div>
      </div>
    </div>
  );
}

// ── CategoryTile ───────────────────────────────────────────

interface CategoryTileProps {
  icon: IconName;
  title: string;
  count: number;
  accent: string;
}

function CategoryTile({ icon, title, count, accent }: CategoryTileProps) {
  return (
    <button
      className="rounded-2xl p-3.5 flex flex-col items-start gap-3 text-left"
      style={{
        background: COLORS.card,
        border: `1px solid ${COLORS.line}`,
        minHeight: 116,
      }}
    >
      <div
        className="w-10 h-10 rounded-xl flex items-center justify-center"
        style={{ background: `${accent}1f`, color: accent }}
      >
        <Icon name={icon} size={20} />
      </div>
      <div className="flex-1">
        <div
          className="text-[13.5px] font-semibold leading-[1.15]"
          style={{ color: COLORS.text }}
        >
          {title}
        </div>
        <div className="text-[11px] mt-0.5" style={{ color: COLORS.textMute }}>
          {count} courses
        </div>
      </div>
    </button>
  );
}

// ── LearnHub ───────────────────────────────────────────────

export function LearnHub() {
  return (
    <div
      className="abc-screen relative h-full flex flex-col"
      style={{ background: COLORS.bg, color: COLORS.text }}
    >
      <ScreenHeader title="Learn Hub" kicker="Cultiver le savoir">
        <SearchBar
          placeholder="Search courses & topics…"
          accessory={
            <button
              className="w-11 h-11 rounded-2xl flex items-center justify-center"
              style={{
                background: COLORS.card,
                border: `1px solid ${COLORS.line}`,
                color: COLORS.text,
              }}
            >
              <Icon name="sliders" size={17} stroke={2} />
            </button>
          }
        />
      </ScreenHeader>

      <div className="flex-1 overflow-y-auto pb-28 scrollbar-hide">
        {/* My Courses */}
        <section className="mt-3">
          <div className="px-5 flex items-center justify-between mb-2.5">
            <h2
              className="text-[16px] font-bold"
              style={{ color: COLORS.text }}
            >
              My Courses
            </h2>
            <button
              className="text-[12px] font-semibold"
              style={{ color: COLORS.terracotta }}
            >
              See all
            </button>
          </div>
          <div className="flex gap-3 overflow-x-auto px-5 scrollbar-hide pb-1">
            <CourseCard
              title="Architect Principles"
              sub="Foundations"
              progress={60}
              color="layers"
              accent={COLORS.green}
            />
            <CourseCard
              title="Financial Literacy"
              sub="Numbers"
              progress={30}
              color="landmark"
              accent={COLORS.green}
            />
            <CourseCard
              title="Brand Storytelling"
              sub="Marketing"
              progress={12}
              color="megaphone"
              accent={COLORS.terracotta}
            />
          </div>
        </section>

        {/* Recommended */}
        <section className="mt-6">
          <div className="px-5 flex items-center justify-between mb-2.5">
            <h2
              className="text-[16px] font-bold"
              style={{ color: COLORS.text }}
            >
              Recommended for You
            </h2>
            <Icon name="sparkles" size={16} style={{ color: COLORS.terracotta }} />
          </div>
          <div className="flex gap-3 overflow-x-auto px-5 scrollbar-hide pb-1">
            <RecCard
              title="System Building"
              sub="Cooperative Foundations"
              tex="tex-weave"
              badge="featured"
            />
            <RecCard
              title="Brand Storytelling"
              sub="Marketing & Comm"
              tex="tex-loom"
              badge="new"
            />
            <RecCard
              title="Regenerative Finance"
              sub="Money as Soil"
              tex="tex-garden"
              badge="advanced"
            />
          </div>
        </section>

        {/* Categories */}
        <section className="mt-7 px-5">
          <h2 className="text-[16px] font-bold mb-3" style={{ color: COLORS.text }}>
            Course Categories
          </h2>
          <div className="grid grid-cols-2 gap-3">
            <CategoryTile
              icon="layers"
              title="Architect Principles"
              count={14}
              accent={COLORS.green}
            />
            <CategoryTile
              icon="users"
              title="System Building"
              count={9}
              accent={COLORS.terracotta}
            />
            <CategoryTile
              icon="megaphone"
              title="Brand Storytelling"
              count={11}
              accent="#d4b042"
            />
            <CategoryTile
              icon="landmark"
              title="Financial Literacy"
              count={18}
              accent={COLORS.green}
            />
            <CategoryTile
              icon="leaf"
              title="Sustainable Practices"
              count={8}
              accent="#5a9f6c"
            />
            <CategoryTile
              icon="sun"
              title="Solarpunk Principles"
              count={6}
              accent={COLORS.terracotta}
            />
          </div>
        </section>
      </div>
    </div>
  );
}

export default LearnHub;

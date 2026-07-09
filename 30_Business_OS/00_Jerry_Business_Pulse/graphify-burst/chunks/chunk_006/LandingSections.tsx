'use client';

import { useState } from 'react';
import { Icon } from './Icon';
import type { IconName } from './Icon';
import { EmbeddedPhone } from './EmbeddedPhone';
import { Avatar } from './Avatar';
import type { TabKey } from '@/lib/types';
import { useTranslations } from 'next-intl';

const PARTNER_NAMES = [
  'Solaris Agri-Coop · Kenya',
  'Umoja Weavers · Tanzania',
  'Sahel Solar Builders · Mali',
  "Kola Roasters · Côte d'Ivoire",
  'Baobab Treasury · Sénégal',
  'Mboga Greens · Rwanda',
  'Sankofa Studio · Ghana',
  'Atlas Looms · Maroc',
];

export function Marquee() {
  const t = useTranslations('marquee');
  const row = [...PARTNER_NAMES, ...PARTNER_NAMES];
  return (
    <section
      className="relative py-8"
      style={{
        borderTop: '1px solid var(--line)',
        borderBottom: '1px solid var(--line)',
        background: 'rgba(18,17,16,0.5)',
        zIndex: 2,
      }}
    >
      <div className="flex items-center gap-6 px-6 mx-auto" style={{ maxWidth: 1200 }}>
        <div
          className="text-[10.5px] uppercase tracking-[0.24em] font-bold flex-shrink-0"
          style={{ color: '#6b6258' }}
        >
          {t('label')}
        </div>
        <div
          className="flex-1 overflow-hidden"
          style={{ maskImage: 'linear-gradient(90deg, transparent, black 8%, black 92%, transparent)' }}
        >
          <div
            className="anim-marquee flex gap-10 whitespace-nowrap"
            style={{ width: 'max-content' }}
          >
            {row.map((n, i) => (
              <span
                key={i}
                className="flex items-center gap-3 text-[14px]"
                style={{ color: '#a89c8a' }}
              >
                <span className="w-1.5 h-1.5 rounded-full" style={{ background: '#e15f41' }} />
                {n}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

export function Manifesto() {
  const t = useTranslations('manifesto');
  return (
    <section id="manifesto" className="relative py-28" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1100 }}>
        <div className="grid md:grid-cols-[1fr_2fr] gap-14">
          <div>
            <div className="eyebrow">{t('eyebrow')}</div>
            <h2
              className="display text-[42px] md:text-[52px] leading-[1.0] mt-5"
              style={{ letterSpacing: '-0.015em' }}
            >
              {t('headline1')}
              <br />
              <span className="ital" style={{ color: '#10b981' }}>
                {t('headlineEm')}
              </span>
            </h2>
          </div>
          <div className="text-[18px] md:text-[20px] leading-[1.5]" style={{ color: '#d8cdbb' }}>
            <p>
              {t('p1Lead')}
              <em className="font-serif ital" style={{ color: '#e15f41' }}>
                {t('p1Em')}
              </em>
              {t('p1Tail')}
            </p>
            <p className="mt-5">
              {t('p2Lead')}
              <em className="font-serif ital">{t('p2Em')}</em>
              {t('p2Tail')}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

const PILLAR_DEFS: ReadonlyArray<{
  key: TabKey;
  icon: IconName;
  titleKey: 'community' | 'learn' | 'build' | 'brand';
  accent: string;
}> = [
  { key: 'community', icon: 'users', titleKey: 'community', accent: '#e15f41' },
  { key: 'learn', icon: 'graduationCap', titleKey: 'learn', accent: '#10b981' },
  { key: 'build', icon: 'wrench', titleKey: 'build', accent: '#d4b042' },
  { key: 'brand', icon: 'award', titleKey: 'brand', accent: '#c47a96' },
];

export function PillarRow() {
  const t = useTranslations('pillars');
  return (
    <section id="platform" className="relative py-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="flex items-end justify-between flex-wrap gap-6 mb-10">
          <div>
            <div className="eyebrow">{t('eyebrow')}</div>
            <h2
              className="display text-[44px] md:text-[58px] leading-[1.0] mt-5"
              style={{ letterSpacing: '-0.015em' }}
            >
              {t('headline1')}
              <br />
              <span className="ital">{t('headlineEm')}</span>
              {t('headlineCont')}
            </h2>
          </div>
          <p
            className="max-w-[420px] text-[15.5px] leading-[1.55]"
            style={{ color: '#a89c8a' }}
          >
            {t('lede')}
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-5">
          {PILLAR_DEFS.map((p) => {
            const title = t(`${p.titleKey}.title`);
            const subtitle = t(`${p.titleKey}.subtitle`);
            const desc = t(`${p.titleKey}.desc`);
            return (
              <article
                key={p.key}
                className="rounded-3xl p-7 relative overflow-hidden"
                style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
              >
                <div
                  className="absolute inset-0 pointer-events-none"
                  style={{
                    background: `radial-gradient(400px 200px at 100% 0%, ${p.accent}1f, transparent 70%)`,
                  }}
                />
                <div className="flex items-start justify-between relative">
                  <div
                    className="w-12 h-12 rounded-2xl flex items-center justify-center"
                    style={{ background: `${p.accent}22`, color: p.accent }}
                  >
                    <Icon name={p.icon} size={22} stroke={2} />
                  </div>
                  <div
                    className="text-[10.5px] tracking-[0.22em] uppercase font-bold"
                    style={{ color: p.accent }}
                  >
                    {subtitle}
                  </div>
                </div>
                <h3 className="display text-[36px] mt-5 leading-none">{title}</h3>
                <p
                  className="text-[14.5px] mt-3 leading-[1.5] max-w-[440px]"
                  style={{ color: '#cfc4b3' }}
                >
                  {desc}
                </p>
                <ul
                  className="mt-5 space-y-2 text-[13.5px]"
                  style={{ color: '#a89c8a' }}
                >
                  {(t.raw(`${p.titleKey}.bullets`) as string[]).map((b, i) => (
                    <li key={i} className="flex items-center gap-2.5">
                      <Icon name="check" size={14} stroke={2.5} style={{ color: p.accent }} />
                      {b}
                    </li>
                  ))}
                </ul>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}

const TOUR_TABS: ReadonlyArray<TabKey> = ['community', 'learn', 'build', 'brand'];

export function PhoneTour() {
  const t = useTranslations('tour');
  const [active, setActive] = useState(0);
  return (
    <section
      className="relative py-24"
      style={{
        zIndex: 2,
        background: 'linear-gradient(180deg, transparent 0%, rgba(225,95,65,0.04) 50%, transparent 100%)',
      }}
    >
      <div className="mx-auto px-6" style={{ maxWidth: 1280 }}>
        <div className="flex items-end justify-between flex-wrap gap-6 mb-10">
          <div>
            <div className="eyebrow">{t('eyebrow')}</div>
            <h2 className="display text-[44px] md:text-[58px] leading-[1.0] mt-5">
              {t('headline1')}
              <span className="ital">{t('headlineEm')}</span>
              {t('headlineCont')}
            </h2>
          </div>
          <p
            className="max-w-[440px] text-[15.5px] leading-[1.55]"
            style={{ color: '#a89c8a' }}
          >
            {t('lede')}
          </p>
        </div>

        <div className="relative">
          <div
            style={{
              position: 'absolute',
              left: 0,
              right: 0,
              top: '62%',
              height: 1,
              background: 'linear-gradient(90deg, transparent, rgba(225,95,65,0.45), transparent)',
            }}
          />

          <div className="flex gap-6 lg:gap-10 overflow-x-auto pb-8 px-2 scrollbar-hide justify-start lg:justify-center">
            {TOUR_TABS.map((tab, i) => {
              const isActive = active === i;
              return (
                <div
                  key={tab}
                  onMouseEnter={() => setActive(i)}
                  className="flex-shrink-0 flex flex-col items-center gap-5 cursor-pointer transition-transform duration-500"
                  style={{ transform: isActive ? 'translateY(-12px)' : 'translateY(0)' }}
                >
                  <div
                    className="relative"
                    style={{
                      filter: isActive
                        ? 'drop-shadow(0 40px 50px rgba(0,0,0,0.5))'
                        : 'drop-shadow(0 18px 25px rgba(0,0,0,0.3))',
                      opacity: isActive ? 1 : 0.78,
                      transition: 'all .4s',
                    }}
                  >
                    <EmbeddedPhone tab={tab} width={260} height={560} showNav />
                  </div>
                  <div className="text-center">
                    <div
                      className="text-[10.5px] tracking-[0.22em] uppercase font-bold"
                      style={{ color: isActive ? '#e15f41' : '#6b6258' }}
                    >
                      0{i + 1}
                    </div>
                    <div
                      className="display text-[24px] mt-1"
                      style={{ color: isActive ? '#f5f2eb' : '#a89c8a' }}
                    >
                      {tab.charAt(0).toUpperCase() + tab.slice(1)}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}

export function Stats() {
  const t = useTranslations('stats');
  const items = t.raw('items') as Array<{ n: string; l: string }>;
  return (
    <section
      className="relative py-12"
      style={{ zIndex: 2, borderTop: '1px solid var(--line)', borderBottom: '1px solid var(--line)' }}
    >
      <div
        className="mx-auto px-6 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-y-8 gap-x-6"
        style={{ maxWidth: 1200 }}
      >
        {items.map((s) => (
          <div key={s.l}>
            <div
              className="display text-[44px] leading-none"
              style={{ letterSpacing: '-0.02em' }}
            >
              {s.n}
            </div>
            <div
              className="text-[12px] mt-2 uppercase tracking-[0.16em] font-semibold"
              style={{ color: '#a89c8a' }}
            >
              {s.l}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

const STEP_TEX: ReadonlyArray<'tex-weave' | 'tex-garden' | 'tex-solar'> = [
  'tex-weave',
  'tex-garden',
  'tex-solar',
];

const STEP_ICON: ReadonlyArray<IconName> = ['graduationCap', 'users', 'sun'];

export function Programme() {
  const t = useTranslations('program');
  const steps = t.raw('steps') as Array<{ n: string; title: string; body: string }>;
  return (
    <section id="program" className="relative py-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="text-center mb-14">
          <div className="eyebrow justify-center inline-flex">{t('eyebrow')}</div>
          <h2
            className="display text-[44px] md:text-[64px] leading-[1.0] mt-5"
            style={{ letterSpacing: '-0.015em' }}
          >
            {t('headline1')}
            <span className="ital" style={{ color: '#e15f41' }}>
              {t('headlineEm')}
            </span>
            {t('headlineCont')}
          </h2>
        </div>

        <div className="grid md:grid-cols-3 gap-5">
          {steps.map((s, i) => (
            <div
              key={s.n}
              className={`rounded-3xl overflow-hidden relative ${STEP_TEX[i] ?? 'tex-weave'}`}
              style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
            >
              <div style={{ height: 140, position: 'relative' }}>
                <div
                  style={{
                    position: 'absolute',
                    inset: 0,
                    background: 'linear-gradient(180deg, transparent 30%, rgba(24,22,20,0.95) 100%)',
                  }}
                />
                <div className="absolute top-4 left-5 right-5 flex items-start justify-between">
                  <div className="text-[10.5px] tracking-[0.24em] uppercase font-bold text-white opacity-90">
                    {t('actLabel')} {s.n}
                  </div>
                  <div
                    className="w-11 h-11 rounded-2xl flex items-center justify-center"
                    style={{ background: 'rgba(0,0,0,0.4)', backdropFilter: 'blur(6px)', color: '#fff' }}
                  >
                    <Icon name={STEP_ICON[i] ?? 'sparkles'} size={20} />
                  </div>
                </div>
                <div className="absolute bottom-3 left-5">
                  <div className="display text-[40px] leading-none" style={{ color: '#fff' }}>
                    {s.title}
                  </div>
                </div>
              </div>
              <div className="p-6">
                <p
                  className="text-[14.5px] leading-[1.55]"
                  style={{ color: '#cfc4b3' }}
                >
                  {s.body}
                </p>
                <div
                  className="mt-5 inline-flex items-center gap-1.5 text-[12.5px] font-semibold"
                  style={{ color: '#e15f41' }}
                >
                  {t('learnMore')} <Icon name="arrowRight" size={13} />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function Testimonials() {
  const t = useTranslations('testimonials');
  return (
    <section id="cooperatives" className="relative py-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="grid lg:grid-cols-[1fr_1fr] gap-5">
          <article
            className="rounded-3xl p-9 md:p-12 relative overflow-hidden"
            style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
          >
            <div
              className="absolute inset-0 pointer-events-none"
              style={{
                background: 'radial-gradient(500px 300px at 0% 0%, rgba(16,185,129,0.10), transparent 60%)',
              }}
            />
            <div
              className="display text-[120px] leading-none"
              style={{ color: '#e15f41', height: 60 }}
            >
              &ldquo;
            </div>
            <blockquote
              className="display text-[26px] md:text-[34px] leading-[1.2] mt-3"
              style={{ letterSpacing: '-0.005em' }}
              dangerouslySetInnerHTML={{ __html: t('quote1') }}
            />
            <div className="flex items-center gap-3 mt-8">
              <Avatar initials="NN" hue={320} size={48} />
              <div>
                <div className="font-semibold text-[15px]">{t('author1Name')}</div>
                <div className="text-[12.5px]" style={{ color: '#a89c8a' }}>
                  {t('author1Role')}
                </div>
              </div>
            </div>
          </article>

          <div className="flex flex-col gap-5">
            <article
              className="rounded-3xl p-7 relative"
              style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
            >
              <div className="flex items-start gap-3">
                <Avatar initials="AO" hue={28} size={44} />
                <div>
                  <div className="font-semibold text-[15px]">{t('author2Name')}</div>
                  <div className="text-[12px]" style={{ color: '#a89c8a' }}>
                    {t('author2Role')}
                  </div>
                </div>
              </div>
              <p
                className="text-[15px] mt-4 leading-[1.5]"
                style={{ color: '#d8cdbb' }}
                dangerouslySetInnerHTML={{ __html: t('quote2') }}
              />
            </article>
            <article
              className="rounded-3xl p-7 relative"
              style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
            >
              <div className="flex items-start gap-3">
                <Avatar initials="KP" hue={210} size={44} />
                <div>
                  <div className="font-semibold text-[15px]">{t('author3Name')}</div>
                  <div className="text-[12px]" style={{ color: '#a89c8a' }}>
                    {t('author3Role')}
                  </div>
                </div>
              </div>
              <p
                className="text-[15px] mt-4 leading-[1.5]"
                style={{ color: '#d8cdbb' }}
                dangerouslySetInnerHTML={{ __html: t('quote3') }}
              />
            </article>
          </div>
        </div>
      </div>
    </section>
  );
}

export function FAQ() {
  const t = useTranslations('faq');
  const items = t.raw('items') as Array<{ q: string; a: string }>;
  const [open, setOpen] = useState(0);
  return (
    <section id="faq" className="relative py-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 980 }}>
        <div className="text-center mb-12">
          <div className="eyebrow justify-center inline-flex">{t('eyebrow')}</div>
          <h2 className="display text-[44px] md:text-[56px] leading-[1.0] mt-5">
            {t('headline1')}
            <span className="ital">{t('headlineEm')}</span>
            {t('headlineCont')}
          </h2>
        </div>
        <div
          className="rounded-3xl overflow-hidden"
          style={{ background: 'var(--card)', border: '1px solid var(--line)' }}
        >
          {items.map((f, i) => {
            const isOpen = open === i;
            return (
              <button
                key={i}
                type="button"
                onClick={() => setOpen(isOpen ? -1 : i)}
                className="w-full text-left px-6 py-5 flex items-start gap-4"
                style={{
                  borderBottom: i === items.length - 1 ? 'none' : '1px solid var(--line)',
                  background: 'transparent',
                  color: 'inherit',
                }}
              >
                <div className="flex-1">
                  <div className="text-[16px] font-semibold flex items-center justify-between gap-4">
                    {f.q}
                    <Icon
                      name="chevronDown"
                      size={18}
                      style={{
                        color: '#a89c8a',
                        transform: isOpen ? 'rotate(180deg)' : 'none',
                        transition: 'transform .2s',
                      }}
                    />
                  </div>
                  <div
                    style={{
                      maxHeight: isOpen ? 220 : 0,
                      opacity: isOpen ? 1 : 0,
                      overflow: 'hidden',
                      transition: 'all .35s ease',
                    }}
                  >
                    <p
                      className="text-[14.5px] mt-3 leading-[1.55]"
                      style={{ color: '#cfc4b3' }}
                    >
                      {f.a}
                    </p>
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export function CTABand() {
  const t = useTranslations('cta');
  const [email, setEmail] = useState('');
  const [sent, setSent] = useState(false);
  return (
    <section id="join" className="relative py-28" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1100 }}>
        <div
          className="rounded-[36px] relative overflow-hidden p-10 md:p-16"
          style={{ background: '#181614', border: '1px solid var(--line)' }}
        >
          <div
            style={{
              position: 'absolute',
              right: -180,
              top: -180,
              width: 520,
              height: 520,
              borderRadius: '50%',
              background:
                'radial-gradient(50% 50% at 50% 50%, rgba(225,95,65,0.45), rgba(225,95,65,0) 70%)',
            }}
          />
          <svg
            style={{ position: 'absolute', right: -60, top: -60, opacity: 0.4 }}
            width="400"
            height="400"
            viewBox="0 0 400 400"
          >
            {Array.from({ length: 30 }).map((_, i) => {
              const a = (i * Math.PI * 2) / 30;
              const x1 = 200 + Math.cos(a) * 140;
              const y1 = 200 + Math.sin(a) * 140;
              const x2 = 200 + Math.cos(a) * 200;
              const y2 = 200 + Math.sin(a) * 200;
              return (
                <line
                  key={i}
                  x1={x1}
                  y1={y1}
                  x2={x2}
                  y2={y2}
                  stroke="#e15f41"
                  strokeWidth="1"
                  opacity={i % 3 === 0 ? 0.7 : 0.3}
                />
              );
            })}
          </svg>

          <div className="relative max-w-[640px]">
            <div className="eyebrow">{t('eyebrow')}</div>
            <h2
              className="display text-[48px] md:text-[68px] leading-[0.98] mt-5"
              style={{ letterSpacing: '-0.015em' }}
            >
              {t('headline1')}
              <br />
              <span className="ital" style={{ color: '#e15f41' }}>
                {t('headlineEm1')}
              </span>
              ,
              <br />
              <span className="ital" style={{ color: '#10b981' }}>
                {t('headlineEm2')}
              </span>
              .
            </h2>
            <p
              className="mt-7 text-[16px] max-w-[480px] leading-[1.55]"
              style={{ color: '#cfc4b3' }}
            >
              {t('lede')}
            </p>

            <form
              onSubmit={(e) => {
                e.preventDefault();
                setSent(true);
              }}
              className="mt-8 flex flex-col sm:flex-row gap-2.5 max-w-[520px]"
            >
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder={t('emailPlaceholder')}
                className="flex-1 h-14 px-5 rounded-full text-[15px] outline-none"
                style={{
                  background: 'rgba(245,242,235,0.05)',
                  color: '#f5f2eb',
                  border: '1px solid rgba(245,242,235,0.12)',
                }}
              />
              <button
                type="submit"
                className="h-14 px-6 rounded-full font-semibold text-[15px] inline-flex items-center justify-center gap-2"
                style={{
                  background: 'linear-gradient(180deg, #e15f41 0%, #d95436 100%)',
                  color: '#fff',
                  boxShadow: '0 18px 30px -12px rgba(225,95,65,0.55)',
                }}
              >
                {sent ? (
                  <>{t('submitSent')}</>
                ) : (
                  <>
                    {t('submitCta')} <Icon name="arrowRight" size={15} />
                  </>
                )}
              </button>
            </form>
            <div className="mt-3 text-[12px]" style={{ color: '#6b6258' }}>
              {t('legalNote')}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export function Footer() {
  const t = useTranslations('footer');
  const platformLinks = t.raw('platformLinks') as string[];
  const programLinks = t.raw('programLinks') as string[];
  const houseLinks = t.raw('houseLinks') as string[];

  const groups: ReadonlyArray<{ title: string; links: string[] }> = [
    { title: t('platform'), links: platformLinks },
    { title: t('program'), links: programLinks },
    { title: t('house'), links: houseLinks },
  ];

  return (
    <footer
      className="relative pt-16 pb-10"
      style={{ zIndex: 2, borderTop: '1px solid var(--line)' }}
    >
      <div
        className="mx-auto px-6 grid md:grid-cols-[1.4fr_1fr_1fr_1fr] gap-10"
        style={{ maxWidth: 1200 }}
      >
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-[15px] tracking-[0.18em]">ABC&nbsp;OS</span>
          </div>
          <p
            className="mt-4 text-[13px] leading-[1.55] max-w-[300px]"
            style={{ color: '#a89c8a' }}
          >
            {t('tagline')}
          </p>
        </div>
        {groups.map((g) => (
          <div key={g.title}>
            <div
              className="text-[10.5px] tracking-[0.22em] uppercase font-bold mb-3"
              style={{ color: '#6b6258' }}
            >
              {g.title}
            </div>
            <ul className="space-y-2.5 text-[13.5px]" style={{ color: '#cfc4b3' }}>
              {g.links.map((l) => (
                <li key={l}>
                  <a href="#" className="hover:text-white transition-colors">
                    {l}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
      <div
        className="mx-auto px-6 mt-12 pt-6 flex flex-wrap items-center justify-between gap-3"
        style={{ maxWidth: 1200, borderTop: '1px solid var(--line)' }}
      >
        <div className="text-[12px]" style={{ color: '#6b6258' }}>
          {t('copyright')} ·{' '}
          <a href="#" className="underline" style={{ color: '#a89c8a' }}>
            {t('license')}
          </a>
        </div>
        <div className="flex items-center gap-4 text-[12px]" style={{ color: '#6b6258' }}>
          <span>{t('motto')}</span>
          <span style={{ width: 6, height: 6, borderRadius: 99, background: '#e15f41' }} />
          <span>{t('origin')}</span>
        </div>
      </div>
    </footer>
  );
}

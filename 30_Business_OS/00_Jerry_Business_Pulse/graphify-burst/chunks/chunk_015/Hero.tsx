import { getTranslations } from 'next-intl/server';
import { Icon } from './Icon';
import { HeroPhone } from './HeroPhone';

export async function Hero() {
  const t = await getTranslations('hero');

  return (
    <section className="relative pt-12 md:pt-20 pb-24" style={{ zIndex: 2 }}>
      <div className="mx-auto px-6" style={{ maxWidth: 1200 }}>
        <div className="grid lg:grid-cols-[1.05fr_1fr] gap-12 items-center">
          <div className="anim-fade-up">
            <div className="eyebrow">{t('eyebrow')}</div>
            <h1
              className="display mt-5 text-[58px] md:text-[78px] leading-[0.94]"
              style={{ letterSpacing: '-0.015em' }}
            >
              {t('headline1')}
              <span className="ital">{t('headline1Em')}</span>
              {t('headline1Cont')}
              <span className="ital">{t('headline2Em')}</span>
              {t('headline2Cont')}
              <br />
              {t('headline3')}
              <br />
              <span style={{ color: '#e15f41' }}>{t('headline4')}</span>
            </h1>
            <p
              className="mt-7 text-[16px] md:text-[17px] leading-[1.55] max-w-[520px]"
              style={{ color: '#cfc4b3' }}
            >
              {t('lede')}
            </p>

            <div className="mt-9 flex flex-wrap gap-3">
              <a
                href="#join"
                className="anim-pulse-btn inline-flex items-center gap-2 h-14 px-6 rounded-full font-semibold text-[15px]"
                style={{
                  background: 'linear-gradient(180deg, #e15f41 0%, #d95436 100%)',
                  color: '#fff',
                  boxShadow: '0 18px 30px -12px rgba(225,95,65,0.55)',
                }}
              >
                {t('primaryCta')} <Icon name="arrowRight" size={16} />
              </a>
              <a
                href="/launch"
                className="inline-flex items-center gap-2 h-14 px-6 rounded-full font-semibold text-[15px] hover:bg-white/10 transition-colors"
                style={{
                  background: 'rgba(245,242,235,0.04)',
                  color: '#f5f2eb',
                  border: '1px solid rgba(245,242,235,0.1)',
                }}
              >
                {t('secondaryCta')} ↗
              </a>
            </div>

            <div
              className="mt-10 flex flex-wrap items-center gap-x-7 gap-y-3 text-[12.5px]"
              style={{ color: '#a89c8a' }}
            >
              <div className="flex items-center gap-2">
                <span
                  className="anim-pulse-dot"
                  style={{
                    width: 8,
                    height: 8,
                    borderRadius: 99,
                    background: '#10b981',
                    boxShadow: '0 0 12px #10b981',
                  }}
                />
                <span>
                  <span style={{ color: '#f5f2eb', fontWeight: 700 }}>2 348</span> {t('trustActive')}
                </span>
              </div>
              <div>
                ·{' '}
                <span style={{ color: '#f5f2eb', fontWeight: 700 }}>124</span> {t('trustCooperatives')}
              </div>
              <div>
                ·{' '}
                <span style={{ color: '#f5f2eb', fontWeight: 700 }}>17</span> {t('trustCountries')}
              </div>
            </div>
          </div>

          <div className="flex justify-center lg:justify-end relative">
            <HeroPhone />
          </div>
        </div>
      </div>
    </section>
  );
}

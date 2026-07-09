import { getTranslations } from 'next-intl/server';
import { LogoMark } from './LogoMark';
import { Icon } from './Icon';
import { LocaleSwitcher } from '@/i18n/LocaleSwitcher';
import { cookies } from 'next/headers';
import { routing } from '@/i18n/routing';

export async function TopNav() {
  const t = await getTranslations('nav');
  const cookieStore = await cookies();
  const current = cookieStore.get('NEXT_LOCALE')?.value ?? routing.defaultLocale;

  return (
    <div
      className="topnav rounded-full mx-auto flex items-center justify-between px-3 py-2"
      style={{ maxWidth: 1180 }}
    >
      <div className="pl-3 flex items-center gap-2">
        <LogoMark size={26} />
        <span className="font-bold text-[15px] tracking-[0.18em]">ABC&nbsp;OS</span>
      </div>
      <nav
        className="hidden md:flex items-center gap-7 text-[13px] font-medium"
        style={{ color: '#cfc4b3' }}
      >
        <a href="#manifesto" className="hover:text-white transition-colors">
          {t('manifesto')}
        </a>
        <a href="#platform" className="hover:text-white transition-colors">
          {t('platform')}
        </a>
        <a href="#program" className="hover:text-white transition-colors">
          {t('program')}
        </a>
        <a href="#cooperatives" className="hover:text-white transition-colors">
          {t('cooperatives')}
        </a>
        <a href="#faq" className="hover:text-white transition-colors">
          {t('faq')}
        </a>
      </nav>
      <div className="flex items-center gap-2">
        <LocaleSwitcher currentLocale={current} />
        <a
          href="/launch"
          className="hidden sm:block text-[13px] font-medium px-3 py-2 rounded-full hover:text-white transition-colors"
          style={{ color: '#cfc4b3' }}
        >
          {t('launchOs')} ↗
        </a>
        <a
          href="#join"
          className="text-[13px] font-semibold px-4 h-10 rounded-full inline-flex items-center gap-1.5"
          style={{
            background: '#e15f41',
            color: '#fff',
            boxShadow: '0 8px 22px -8px rgba(225,95,65,0.6)',
          }}
        >
          {t('join')} <Icon name="arrowRight" size={14} />
        </a>
      </div>
    </div>
  );
}

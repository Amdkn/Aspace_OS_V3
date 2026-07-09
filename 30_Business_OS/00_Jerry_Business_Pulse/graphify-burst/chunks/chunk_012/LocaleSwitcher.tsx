'use client';

import { useTransition } from 'react';
import { useRouter } from './navigation';

const LOCALE_LABELS: Record<string, { short: string; full: string }> = {
  fr: { short: 'FR', full: 'Français' },
  en: { short: 'EN', full: 'English' },
};

interface LocaleSwitcherProps {
  currentLocale: string;
}

export function LocaleSwitcher({ currentLocale }: LocaleSwitcherProps) {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();

  const nextLocale = currentLocale === 'fr' ? 'en' : 'fr';

  const handleSwitch = () => {
    document.cookie = `NEXT_LOCALE=${nextLocale};path=/;max-age=31536000`;
    startTransition(() => {
      router.refresh();
    });
  };

  return (
    <button
      type="button"
      onClick={handleSwitch}
      disabled={isPending}
      aria-label={`Switch language to ${LOCALE_LABELS[nextLocale]?.full ?? nextLocale}`}
      className="inline-flex items-center justify-center h-9 px-3 rounded-full text-[12px] font-semibold tracking-[0.18em] uppercase transition-colors"
      style={{
        background: 'rgba(245,242,235,0.05)',
        border: '1px solid rgba(245,242,235,0.12)',
        color: '#f5f2eb',
        cursor: isPending ? 'wait' : 'pointer',
      }}
    >
      {LOCALE_LABELS[nextLocale]?.short ?? nextLocale}
    </button>
  );
}

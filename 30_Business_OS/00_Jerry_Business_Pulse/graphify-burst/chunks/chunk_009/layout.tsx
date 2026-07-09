import type { Metadata, Viewport } from 'next';
import { Geist_Mono } from 'next/font/google';
import { getLocale, getTranslations } from 'next-intl/server';
import { NextIntlClientProvider } from 'next-intl';
import './globals.css';

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
  display: 'swap',
});

export async function generateMetadata(): Promise<Metadata> {
  const t = await getTranslations('meta');
  return {
    title: {
      default: t('siteTitle'),
      template: '%s · ABC OS',
    },
    description: t('siteDescription'),
    applicationName: 'ABC OS',
    authors: [{ name: 'ABC OS Collective' }],
    keywords: [
      'African cooperatives',
      'solarpunk',
      'cooperation',
      'coopératives africaines',
      'régénératif',
    ],
    openGraph: {
      title: t('ogTitle'),
      description: t('ogDescription'),
      type: 'website',
      locale: 'fr_FR',
      siteName: 'ABC OS',
    },
    twitter: {
      card: 'summary_large_image',
      title: t('ogTitle'),
      description: t('ogDescription'),
    },
  };
}

export const viewport: Viewport = {
  themeColor: '#0c0b0a',
  width: 'device-width',
  initialScale: 1,
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const locale = await getLocale();
  return (
    <html
      lang={locale}
      className={`${geistMono.variable} h-full antialiased`}
      style={{
        // Local fallbacks — we declare CSS variables consumed by tokens.ts
        // (--font-manrope, --font-instrument-serif) so the rest of the design
        // system can reference them without a network round-trip.
        ['--font-manrope' as string]:
          "'Manrope', -apple-system, 'Segoe UI', system-ui, sans-serif",
        ['--font-instrument-serif' as string]:
          "'Instrument Serif', 'Iowan Old Style', Georgia, serif",
      }}
    >
      <body className="min-h-full flex flex-col">
        <NextIntlClientProvider>{children}</NextIntlClientProvider>
      </body>
    </html>
  );
}

import type { Metadata } from "next";
import { Cormorant_Garamond, Hanken_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";
import { colors, fonts } from "@/design/tokens";

const cormorant = Cormorant_Garamond({
  variable: "--font-cormorant",
  subsets: ["latin"],
  weight: ["500", "600", "700"],
  style: ["normal", "italic"],
  display: "swap",
});

const hanken = Hanken_Grotesk({
  variable: "--font-hanken",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

const jetbrains = JetBrains_Mono({
  variable: "--font-jetbrains",
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Nexus · Agentic Governance · Zero-PII by default",
  description:
    "Vous signez le mandat. Nous exécutons en silence dans votre vault privé. Zero-PII by default. AI-Act ready. Sober 1an+.",
  openGraph: {
    title: "Nexus · Agentic Governance · Zero-PII by default",
    description:
      "Vous signez le mandat. Nous exécutons en silence dans votre vault privé. Zero-PII by default. AI-Act ready. Sober 1an+.",
    type: "website",
    locale: "fr_FR",
  },
  themeColor: colors.bg,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="fr"
      className={`${cormorant.variable} ${hanken.variable} ${jetbrains.variable}`}
    >
      <body
        className="min-h-screen overflow-x-hidden antialiased"
        style={{
          background: colors.bg,
          color: colors.cream,
          fontFamily: fonts.sans,
        }}
      >
        <div className="nx-grain" />
        <div style={{ position: "relative", zIndex: 2 }}>{children}</div>
      </body>
    </html>
  );
}

import type { Metadata } from "next";
import { Space_Grotesk, Inter, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const spaceGrotesk = Space_Grotesk({
  variable: "--font-display",
  subsets: ["latin"],
});

const inter = Inter({
  variable: "--font-sans",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "OMK Services — Business OS & Operational Engineering",
  description: "Ingénierie opérationnelle pour Small Business Owners. Déployez votre Business OS et transformez votre entreprise manuelle en système autonome.",
  keywords: ["Business OS", "Automatisation", "No-Code", "CRM", "SOP", "Small Business", "OMK Services"],
  authors: [{ name: "OMK Services" }],
  creator: "OMK Services",
  publisher: "OMK Services",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  openGraph: {
    title: "OMK Services — Empowering Small Business Owners",
    description: "Arrêtez de travailler dans votre entreprise. Travaillez sur elle. Déployez un Business OS clé en main.",
    url: "https://omk.services",
    siteName: "OMK Services",
    locale: "fr_FR",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "OMK Services — Business OS",
    description: "Ingénierie opérationnelle pour Small Business Owners.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="fr"
      className={`${spaceGrotesk.variable} ${inter.variable} ${jetbrainsMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-ink-950 text-slate-200">
        {children}
      </body>
    </html>
  );
}

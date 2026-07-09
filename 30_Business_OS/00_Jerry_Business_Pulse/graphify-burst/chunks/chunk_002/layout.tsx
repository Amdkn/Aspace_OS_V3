import type { Metadata } from "next";
import { Instrument_Serif, JetBrains_Mono, Geist } from "next/font/google";
import "./globals.css";

const instrumentSerif = Instrument_Serif({
  weight: "400",
  subsets: ["latin"],
  style: ["normal", "italic"],
  variable: "--font-display",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  weight: ["300", "400", "500"],
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
});

const geist = Geist({
  weight: ["300", "400", "500", "600"],
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Solaris · AaaS · You're not buying software, you're buying a factory",
  description:
    "Solaris is an Agency-as-a-Service — a white-label production infrastructure. A ghost factory running under your logo. Scale your operations, protect your margins, without ever growing your payroll.",
  keywords: [
    "Agency as a Service",
    "AaaS",
    "white label agency",
    "AI automation agency",
    "production infrastructure",
    "Solaris",
  ],
  openGraph: {
    title: "Solaris · Agency-as-a-Service",
    description:
      "Stop hiring operators. Plug into our factory. White-label production infrastructure for agencies.",
    type: "website",
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: "Solaris · AaaS",
    description: "Stop hiring operators. Plug into our factory.",
  },
  robots: { index: true, follow: true },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${instrumentSerif.variable} ${jetbrainsMono.variable} ${geist.variable}`}
      data-archetype="aaa"
      data-density="comfortable"
    >
      <body>{children}</body>
    </html>
  );
}

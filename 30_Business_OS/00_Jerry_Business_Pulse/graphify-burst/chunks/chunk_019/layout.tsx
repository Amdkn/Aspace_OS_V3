import type { Metadata } from "next";
import { Inter, Cinzel } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

const cinzel = Cinzel({
  subsets: ["latin"],
  variable: "--font-cinzel",
});

export const metadata: Metadata = {
  title: {
    default: "Alikaly Bana Holding | Sovereign Asset Protocol",
    template: "%s | Alikaly Bana Holding",
  },
  description: "Architecting Value in Real Estate Assets. Algorithmic asset recovery and strategic land acquisition powered by the proprietary SOB Engine™.",
  openGraph: {
    title: "Alikaly Bana Holding",
    description: "Sovereign Asset Protocol v4.0",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${cinzel.variable}`}>
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}

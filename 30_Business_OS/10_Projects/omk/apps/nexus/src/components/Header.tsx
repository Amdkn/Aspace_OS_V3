"use client";

import { fonts } from "@/design/tokens";

interface HeaderProps {
  onScrollToForm: () => void;
}

const NAV_ITEMS = [
  { id: "s01", label: "01 Manifeste" },
  { id: "s02", label: "02 Anatomy" },
  { id: "s03", label: "03 Trust" },
  { id: "s04", label: "04 Cabinets" },
  { id: "s05", label: "05 Profiles" },
  { id: "s06", label: "06 Levers" },
  { id: "s07", label: "07 Onboarding" },
];

export default function Header({ onScrollToForm }: HeaderProps) {
  return (
    <header
      className="sticky top-0 z-50 flex items-center justify-between gap-6 px-6 py-[18px] md:px-10"
      style={{
        background: "rgba(10,14,22,.72)",
        backdropFilter: "blur(14px)",
        borderBottom: "1px solid rgba(200,165,92,.16)",
      }}
    >
      <div className="flex items-baseline gap-[14px] flex-shrink-0">
        <span
          className="text-2xl font-bold tracking-[.02em] text-[#F5EFE0]"
          style={{ fontFamily: fonts.serif }}
        >
          Nexus
        </span>
        <span
          className="text-[10px] tracking-[.18em] uppercase"
          style={{
            fontFamily: fonts.mono,
            color: "rgba(200,165,92,.7)",
          }}
        >
          the ghost cabinet · vault / sovereign
        </span>
      </div>
      <nav
        className="hidden lg:flex gap-[22px] items-center text-[11px] tracking-[.1em] uppercase"
        style={{
          fontFamily: fonts.mono,
          color: "rgba(245,239,224,.55)",
        }}
      >
        {NAV_ITEMS.map((item) => (
          <a key={item.id} href={`#${item.id}`} className="text-inherit no-underline hover:text-[#F5EFE0] transition-colors">
            {item.label}
          </a>
        ))}
      </nav>
      <button
        onClick={onScrollToForm}
        className="flex-shrink-0 text-[11px] tracking-[.1em] uppercase font-medium cursor-pointer border-0 px-[18px] py-[11px]"
        style={{
          fontFamily: fonts.mono,
          color: "#0A0E16",
          background: "#C8A55C",
        }}
      >
        Soumettre un cabinet
      </button>
    </header>
  );
}

"use client";

import { fonts } from "@/design/tokens";

export default function Footer() {
  return (
    <footer
      className="relative px-6 md:px-10"
      style={{
        paddingTop: 40,
        paddingBottom: 40,
        background: "#050608",
        borderTop: "1px solid rgba(200,165,92,.12)",
      }}
    >
      <div
        className="mx-auto flex justify-between items-center flex-wrap gap-[18px]"
        style={{ maxWidth: "1180px" }}
      >
        <div
          className="text-[11px] tracking-[.06em]"
          style={{
            fontFamily: fonts.mono,
            color: "rgba(245,239,224,.5)",
          }}
        >
          nexus.cabinet · the ghost cabinet · vault / sovereign · async
        </div>
        <div
          className="text-[11px] tracking-[.06em] flex items-center gap-2"
          style={{
            fontFamily: fonts.mono,
            color: "rgba(200,165,92,.6)",
          }}
        >
          <span
            className="rounded-full"
            style={{
              width: 6,
              height: 6,
              background: "#6FA98A",
              animation: "nx-pulse 2s infinite",
            }}
          />
          wave 01 · 2026 · uptime 99.94 · factory online
        </div>
      </div>
    </footer>
  );
}

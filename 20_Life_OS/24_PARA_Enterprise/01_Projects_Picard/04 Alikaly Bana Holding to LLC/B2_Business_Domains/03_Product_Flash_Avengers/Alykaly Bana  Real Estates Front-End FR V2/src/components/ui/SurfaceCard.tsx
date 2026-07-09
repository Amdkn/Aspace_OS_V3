import { ReactNode } from "react";

interface SurfaceCardProps {
  children: ReactNode;
  className?: string;
  hover?: boolean;
}

export default function SurfaceCard({ children, className = "", hover = false }: SurfaceCardProps) {
  return (
    <div
      className={`relative border border-slate-800 bg-slate-950/60 backdrop-blur-sm rounded-sm overflow-hidden ${
        hover ? "expertise-card" : ""
      } ${className}`}
    >
      {children}
    </div>
  );
}
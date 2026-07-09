import React from 'react';
import { PEPITES } from '../constants';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { Bell, User, Eye } from 'lucide-react';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface HeaderProps {
  activeId: string;
  onNavigate: (id: string) => void;
}

const Header: React.FC<HeaderProps> = ({ activeId, onNavigate }) => {
  return (
    <header className="h-[var(--header-height)] glass border-b border-[var(--glass-border)] flex items-center justify-between px-6 z-10 sticky top-0 shadow-lg">
      <div className="flex items-center gap-6 overflow-hidden max-w-[65%]">
        <div className="flex items-center gap-2 group cursor-pointer">
          <Eye className="w-5 h-5 text-[var(--brass)] group-hover:animate-pulse" />
        </div>
        
        <div className="h-6 w-[1px] bg-[var(--glass-border)] shrink-0" />
        
        <nav className="flex items-center gap-1 overflow-x-auto custom-scrollbar no-scrollbar">
          {PEPITES.map((pepite) => {
            const Icon = pepite.icon;
            const isActive = activeId === pepite.id;
            
            return (
              <button
                key={pepite.id}
                onClick={() => onNavigate(pepite.id)}
                className={cn(
                  "px-4 py-1.5 rounded-full flex items-center gap-2 transition-all duration-300 relative group overflow-hidden shrink-0",
                  isActive ? "bg-[var(--glass-bg-active)]" : "hover:bg-[var(--glass-bg-hover)]"
                )}
              >
                <Icon className={cn(
                  "w-3.5 h-3.5 transition-colors",
                  isActive ? "text-[var(--brass)]" : "text-[var(--text-muted)] group-hover:text-white"
                )} />
                <span className={cn(
                  "text-[10px] font-black uppercase tracking-widest whitespace-nowrap",
                  isActive ? "text-white" : "text-[var(--text-muted)] group-hover:text-[var(--text-secondary)]"
                )}>
                  {pepite.label}
                </span>
                {isActive && (
                  <div className="absolute bottom-0 left-0 right-0 h-[1px] bg-gradient-to-r from-transparent via-[var(--brass)] to-transparent" />
                )}
              </button>
            );
          })}
        </nav>
      </div>

      <div className="flex items-center gap-4 shrink-0">
        <div className="flex items-center gap-3">
          <button className="p-2 rounded-lg hover:bg-[var(--glass-bg-hover)] text-[var(--text-muted)] hover:text-white transition-colors relative">
            <Bell className="w-5 h-5" />
            <div className="absolute top-2 right-2 w-1.5 h-1.5 bg-[var(--accent-danger)] rounded-full shadow-[0_0_5px_var(--accent-danger)]" />
          </button>
          
          <div className="h-6 w-[1px] bg-[var(--glass-border)]" />
          
          <div className="flex items-center gap-3 pl-1">
            <div className="text-right hidden sm:block">
              <div className="text-[10px] font-black text-white tracking-[.1em] uppercase">Amadeus</div>
              <div className="text-[9px] text-[var(--brass)] font-black uppercase tracking-widest opacity-80 italic">A0 Overseer</div>
            </div>
            <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-[var(--brass)] to-[var(--copper)] p-[1px] shadow-lg">
              <div className="w-full h-full rounded-[10px] bg-[#020617] flex items-center justify-center">
                <User className="w-5 h-5 text-[var(--brass)]" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;

import React, { useState } from 'react';
import { FRAMEWORKS, SIDEBAR_FOOTER } from '../constants';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { ChevronRight, PanelLeftClose, PanelLeftOpen, FileText, Search, Clock } from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface SideNavProps {
  isCollapsed: boolean;
  onToggle: () => void;
  activeId: string;
  onNavigate: (id: string, subItem?: string) => void;
}

const SideNav: React.FC<SideNavProps> = ({ isCollapsed, onToggle, activeId, onNavigate }) => {
  const [expandedId, setExpandedId] = useState<string | null>(null);

  const handleFrameworkClick = (id: string) => {
    if (isCollapsed) {
      onToggle();
      setExpandedId(id);
      return;
    }
    setExpandedId(expandedId === id ? null : id);
    onNavigate(id);
  };

  return (
    <aside 
      className={cn(
        "h-screen glass border-r border-[var(--glass-border)] flex flex-col transition-all duration-300 relative z-20",
        isCollapsed ? "w-[72px]" : "w-[var(--sidebar-width)]"
      )}
    >
      <div className="h-[var(--header-height)] flex items-center justify-between px-4 border-b border-[var(--glass-border-subtle)]">
        {!isCollapsed && (
          <div className="flex items-center gap-2 overflow-hidden truncate">
            <div className="w-8 h-8 rounded-lg bg-[var(--copper)] border border-[var(--brass)] flex items-center justify-center shrink-0">
              <span className="text-white font-black text-xs">P.1</span>
            </div>
            <span className="text-[10px] font-black tracking-[.2em] text-white uppercase opacity-80">Frameworks</span>
          </div>
        )}
        <button 
          onClick={onToggle}
          className="p-2 rounded-lg hover:bg-[var(--glass-bg-hover)] text-[var(--text-muted)] hover:text-white transition-colors ml-auto"
        >
          {isCollapsed ? <PanelLeftOpen className="w-5 h-5" /> : <PanelLeftClose className="w-5 h-5" />}
        </button>
      </div>

      <nav className="flex-1 p-3 space-y-1 custom-scrollbar overflow-y-auto overflow-x-hidden">
        {FRAMEWORKS.map((fw) => {
          const Icon = fw.icon;
          const isExpanded = expandedId === fw.id;
          const isActive = activeId === fw.id;

          return (
            <div key={fw.id} className="flex flex-col gap-1">
              <button
                onClick={() => handleFrameworkClick(fw.id)}
                title={isCollapsed ? fw.label : undefined}
                className={cn(
                  "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 group relative",
                  isExpanded 
                    ? "bg-[var(--glass-bg-active)] text-white shadow-lg" 
                    : "text-[var(--text-muted)] hover:bg-[var(--glass-bg-hover)] hover:text-[var(--text-secondary)]"
                )}
              >
                <div className="relative">
                  <Icon className={cn(
                    "w-5 h-5 shrink-0 transition-transform duration-300",
                    isExpanded ? "text-[var(--brass)] scale-110" : "group-hover:text-[var(--text-primary)]"
                  )} />
                  {isActive && (
                    <div className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-[var(--brass)] shadow-[0_0_8px_var(--brass)]" />
                  )}
                </div>
                
                {!isCollapsed && (
                  <div className="flex flex-col items-start overflow-hidden text-left flex-1">
                    <span className="text-[11px] font-black tracking-widest uppercase">{fw.label}</span>
                    <span className="text-[9px] text-[var(--text-muted)] truncate w-full opacity-60 font-medium">
                      {fw.description}
                    </span>
                  </div>
                )}

                {!isCollapsed && (
                  <ChevronRight className={cn(
                    "w-3.5 h-3.5 transition-transform duration-300 opacity-40 group-hover:opacity-100",
                    isExpanded && "rotate-90 text-[var(--brass)] opacity-100"
                  )} />
                )}
              </button>

              <AnimatePresence>
                {isExpanded && !isCollapsed && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: "auto", opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    className="overflow-hidden flex flex-col pl-9 pr-2 space-y-0.5"
                  >
                    {fw.subItems?.map((item, idx) => {
                      if (item === '---' || item.startsWith('SEP:')) {
                        const label = item.startsWith('SEP:') ? item.replace('SEP:', '') : null;
                        return (
                          <div key={`sep-${idx}`} className="py-2 px-2">
                            <div className="flex items-center gap-2">
                              <div className="h-px bg-gradient-to-r from-[var(--brass)]/50 to-transparent flex-1 opacity-30" />
                              {label && (
                                <span className="text-[7px] font-black text-[var(--brass)] uppercase tracking-[0.2em] whitespace-nowrap opacity-60">
                                  {label}
                                </span>
                              )}
                            </div>
                          </div>
                        );
                      }
                      
                      const isHorizon = /^H\d+/.test(item);
                      const SubIcon = isHorizon ? Clock : FileText;

                      return (
                        <button
                          key={item}
                          onClick={() => onNavigate(fw.id, item)}
                          className={cn(
                            "flex items-center gap-2 py-1.5 px-2 rounded-lg text-[10px] font-bold transition-all group/item text-left uppercase tracking-wider",
                            isHorizon 
                              ? "text-[var(--brass)] hover:bg-[var(--brass)]/10" 
                              : "text-[var(--text-muted)] hover:text-white hover:bg-[var(--glass-bg-hover)]"
                          )}
                        >
                          <SubIcon className={cn(
                            "w-3 h-3 transition-opacity",
                            isHorizon ? "opacity-80" : "opacity-30 group-hover/item:opacity-80"
                          )} />
                          <span className="truncate">{item}</span>
                        </button>
                      );
                    })}
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}

        {!isCollapsed && (
          <div className="pt-4 pb-2 px-2">
            <div className="relative group">
              <input 
                type="text" 
                placeholder="Search frameworks..." 
                className="bg-[var(--glass-l2-bg)] border border-[var(--glass-l2-border)] rounded-xl px-10 py-2.5 text-[10px] text-white focus:outline-none focus:border-[var(--brass)] transition-all w-full group-hover:bg-[var(--glass-bg-hover)]"
              />
              <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-[var(--text-muted)] group-hover:text-[var(--brass)] transition-colors" />
            </div>
          </div>
        )}

        <div className="pt-2 flex flex-col gap-1">
          {SIDEBAR_FOOTER.map((item) => {
            const Icon = item.icon;
            const isActive = activeId === item.id;

            return (
              <button
                key={item.id}
                onClick={() => onNavigate(item.id)}
                title={isCollapsed ? item.label : undefined}
                className={cn(
                  "w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition-all duration-200 group relative",
                  isActive 
                    ? "bg-[var(--glass-bg-active)] text-white shadow-lg" 
                    : "text-[var(--text-muted)] hover:bg-[var(--glass-bg-hover)] hover:text-[var(--text-secondary)]"
                )}
              >
                <div className="relative">
                  <Icon className={cn(
                    "w-5 h-5 shrink-0 transition-transform duration-300",
                    isActive ? "text-[var(--brass)] scale-110" : "group-hover:text-[var(--text-primary)]"
                  )} />
                  {isActive && (
                    <div className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-[var(--brass)] shadow-[0_0_8px_var(--brass)]" />
                  )}
                </div>
                
                {!isCollapsed && (
                  <div className="flex flex-col items-start overflow-hidden text-left flex-1">
                    <span className="text-[11px] font-black tracking-widest uppercase">{item.label}</span>
                  </div>
                )}
              </button>
            );
          })}
        </div>
      </nav>

      <div className="p-4 border-t border-[var(--glass-border-subtle)] bg-[var(--glass-l2-bg)] flex flex-col gap-3">
        {!isCollapsed ? (
          <>
            <div className="flex flex-col gap-1">
              <span className="text-[9px] font-black text-[var(--brass)] uppercase tracking-widest">A0 Oversight</span>
              <div className="text-[10px] text-[var(--text-muted)] italic leading-tight">
                "The Watcher is active."
              </div>
            </div>
            
            <div className="flex items-center gap-2 px-2 py-1.5 rounded-lg bg-[var(--accent-primary-glow)] border border-[var(--accent-primary)]/20 shadow-sm animate-pulse-slow">
              <div className="w-1.5 h-1.5 rounded-full bg-[var(--accent-primary)] shadow-[0_0_8px_var(--accent-primary)]" />
              <span className="text-[8px] font-black text-[var(--accent-primary)] uppercase tracking-wider">Auto-Sync Active</span>
            </div>
          </>
        ) : (
          <div className="flex flex-col items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-[var(--brass)] animate-pulse" />
            <div className="w-1.5 h-1.5 rounded-full bg-[var(--accent-primary)]" />
          </div>
        )}
      </div>
    </aside>
  );
};

export default SideNav;

import React, { useState } from 'react';
import { 
  LayoutDashboard, 
  Wallet, 
  Users, 
  Database, 
  FolderOpen, 
  Scale, 
  BookOpen, 
  TrendingUp, 
  Lock, 
  Server, 
  Settings,
  ChevronLeft,
  ChevronRight,
  LogOut
} from 'lucide-react';
import { cn } from '../lib/utils';

type NavSection = {
  title: string;
  icon: string;
  items: { name: string; id: string; icon: React.ElementType }[];
};

export function Sidebar({ activeSection, onNavigate }: { activeSection: string, onNavigate: (id: string) => void }) {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const [showProfileMenu, setShowProfileMenu] = useState(false);

  const menuSections: NavSection[] = [
    {
      title: 'CULTIVATE',
      icon: '🌱',
      items: [
        { name: 'Dashboard', id: 'dashboard', icon: LayoutDashboard },
        { name: 'Finance', id: 'finance', icon: Wallet },
        { name: 'People', id: 'people', icon: Users },
      ]
    },
    {
      title: 'NURTURE',
      icon: '🌿',
      items: [
        { name: 'Docket & OSINT', id: 'docket', icon: Database },
        { name: 'Clients', id: 'clients', icon: FolderOpen },
        { name: 'Legal', id: 'legal', icon: Scale },
        { name: 'Knowledge', id: 'knowledge', icon: BookOpen },
      ]
    },
    {
      title: 'BLOOM',
      icon: '🌸',
      items: [
        { name: 'Growth', id: 'growth', icon: TrendingUp },
        { name: 'Sales Sanctum', id: 'sales', icon: Lock },
      ]
    },
    {
      title: 'ROOTS',
      icon: '🌳',
      items: [
        { name: 'System Roots', id: 'system', icon: Server },
        { name: 'Settings', id: 'settings', icon: Settings },
      ]
    }
  ];

  return (
    <div 
      className={cn(
        "relative flex flex-col h-screen bg-stone-950 border-r border-stone-800 transition-all duration-300 ease-in-out shrink-0 z-50",
        isCollapsed ? 'w-20' : 'w-64'
      )}
    >
      {/* Header & Collapse Button */}
      <div className="flex items-center justify-between p-4 mb-2">
        {!isCollapsed && (
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center">
              <Scale size={16} className="text-emerald-500" />
            </div>
            <span className="text-stone-100 font-display font-bold text-lg tracking-wide">Alykaly OS</span>
          </div>
        )}
        {isCollapsed && (
           <div className="w-10 h-10 mx-auto rounded-full bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center">
             <Scale size={18} className="text-emerald-500" />
           </div>
        )}
        
        <button 
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="absolute -right-3 top-6 bg-stone-900 border border-stone-800 rounded-full p-1 text-stone-500 hover:text-emerald-500 hover:border-emerald-500/50 transition-colors z-10"
        >
          {isCollapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
        </button>
      </div>

      {/* Navigation Modules */}
      <div className="flex-1 overflow-y-auto overflow-x-hidden scrollbar-hide px-3">
        {menuSections.map((section, idx) => (
          <div key={idx} className="mb-6">
            {!isCollapsed ? (
              <div className="flex items-center gap-2 mb-3 px-2 text-xs font-bold text-stone-500 tracking-widest uppercase">
                <span>{section.icon}</span>
                <span>{section.title}</span>
              </div>
            ) : (
              <div className="flex justify-center mb-3 text-lg" title={section.title}>
                {section.icon}
              </div>
            )}
            
            <nav className="space-y-1">
              {section.items.map((item, itemIdx) => {
                const isActive = activeSection === item.id;
                return (
                  <button
                    key={itemIdx}
                    onClick={() => onNavigate(item.id)}
                    className={cn(
                      "w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-all duration-200 group relative",
                      isCollapsed ? 'justify-center' : 'justify-start',
                      isActive 
                        ? 'bg-emerald-500/10 text-emerald-500 border border-emerald-500/20' 
                        : 'text-stone-400 hover:bg-stone-900 border border-transparent hover:border-stone-800/50 hover:text-stone-200'
                    )}
                    title={isCollapsed ? item.name : ''}
                  >
                    <span className={cn("transition-colors", isActive ? 'text-emerald-500' : 'group-hover:text-emerald-400')}>
                      <item.icon size={20} />
                    </span>
                    {!isCollapsed && (
                      <span className="text-sm font-medium">{item.name}</span>
                    )}
                  </button>
                );
              })}
            </nav>
          </div>
        ))}
      </div>

      {/* Profile Section (Bottom) */}
      <div className="relative p-4 border-t border-stone-800 bg-stone-950">
        {/* Dropdown Menu (Popup) */}
        {showProfileMenu && !isCollapsed && (
          <div className="absolute bottom-full left-4 right-4 mb-2 bg-stone-900 border border-stone-800 rounded-lg shadow-xl overflow-hidden z-20">
            <button className="w-full flex items-center gap-3 px-4 py-3 text-sm text-stone-300 hover:bg-stone-800 hover:text-stone-100 transition-colors">
              <Settings size={16} />
              System Preferences
            </button>
            <button className="w-full flex items-center gap-3 px-4 py-3 text-sm text-rose-400 hover:bg-rose-500/10 transition-colors border-t border-stone-800">
              <LogOut size={16} />
              Secure Logout
            </button>
          </div>
        )}

        <div 
          onClick={() => !isCollapsed && setShowProfileMenu(!showProfileMenu)}
          className={cn(
            "flex items-center p-2 rounded-lg cursor-pointer hover:bg-stone-900 transition-colors border border-transparent hover:border-stone-800",
            isCollapsed ? 'justify-center' : 'justify-between'
          )}
          title={isCollapsed ? "Architect / System Admin" : ""}
        >
          <div className="flex items-center gap-3">
            {/* Avatar Badge */}
            <div className="w-10 h-10 rounded-md bg-stone-900 border border-emerald-500/30 flex items-center justify-center shrink-0">
              <span className="text-emerald-500 font-display font-bold">AH</span>
            </div>
            
            {/* Name & Role */}
            {!isCollapsed && (
              <div className="flex flex-col text-left">
                <span className="text-sm font-bold text-stone-100">Architect</span>
                <span className="text-xs text-emerald-500/80 font-medium tracking-wide">System Admin</span>
              </div>
            )}
          </div>

          {!isCollapsed && (
            <Settings 
              size={16} 
              className={cn("text-stone-500 transition-transform duration-300", showProfileMenu ? 'rotate-90 text-emerald-500' : '')} 
            />
          )}
        </div>
      </div>
    </div>
  );
}

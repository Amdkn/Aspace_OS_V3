"use client";

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Icons } from '@/components/Icons';

export const BottomNav = () => {
  const pathname = usePathname();

  const NavItem = ({ icon: Icon, label, href }: { icon: any, label: string, href: string }) => {
    if (!Icon) return null;
    const isActive = pathname === href || (href === '/' && pathname === '/dashboard');
    
    return (
      <Link
        href={href}
        className={`flex flex-col items-center justify-center w-full py-2 transition-colors ${isActive ? 'text-blue-600' : 'text-slate-400'}`}
      >
        <Icon size={24} strokeWidth={isActive ? 2.5 : 2} className="mb-1" />
        <span className="text-[10px] font-medium">{label}</span>
      </Link>
    );
  };

  return (
    <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 px-2 pb-safe pt-2 flex justify-between items-center z-50 max-w-md mx-auto">
      <NavItem icon={Icons.Home} label="Accueil" href="/" />
      <NavItem icon={Icons.Calendar} label="Agenda" href="/calendar" />
      <NavItem icon={Icons.Users} label="Annuaire" href="/directory" />
      <NavItem icon={Icons.Settings} label="Réglages" href="/settings" />
    </nav>
  );
};

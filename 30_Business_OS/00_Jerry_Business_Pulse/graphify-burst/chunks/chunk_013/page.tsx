"use client";

import React, { useState } from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Dashboard } from '@/components/Dashboard';
import { Finance } from '@/components/Finance';
import { People } from '@/components/People';
import { Docket } from '@/components/Docket';
import { Clients } from '@/components/Clients';
import { Legal } from '@/components/Legal';
import { Knowledge } from '@/components/Knowledge';
import { Growth } from '@/components/Growth';
import { SalesSanctum } from '@/components/SalesSanctum';
import { SystemRoots } from '@/components/SystemRoots';
import { Settings } from '@/components/Settings';

export default function App() {
  const [activeSection, setActiveSection] = useState('dashboard');

  return (
    <div className="flex h-screen bg-stone-950 overflow-hidden text-stone-300">
      <Sidebar activeSection={activeSection} onNavigate={setActiveSection} />
      
      <main className="flex-1 overflow-y-auto min-w-0">
        {activeSection === 'dashboard' ? (
          <Dashboard />
        ) : activeSection === 'finance' ? (
          <Finance />
        ) : activeSection === 'people' ? (
          <People />
        ) : activeSection === 'docket' ? (
          <Docket />
        ) : activeSection === 'clients' ? (
          <Clients />
        ) : activeSection === 'legal' ? (
          <Legal />
        ) : activeSection === 'knowledge' ? (
          <Knowledge />
        ) : activeSection === 'growth' ? (
          <Growth />
        ) : activeSection === 'sales' ? (
          <SalesSanctum />
        ) : activeSection === 'system' ? (
          <SystemRoots />
        ) : activeSection === 'settings' ? (
          <Settings />
        ) : (
          <div className="p-8 h-full flex flex-col items-center justify-center text-center">
            <div className="w-16 h-16 bg-stone-900 border border-stone-800 rounded-2xl flex items-center justify-center mb-6">
              <span className="text-2xl opacity-50">🚧</span>
            </div>
            <h2 className="text-xl font-display font-medium text-stone-300 mb-2">Module en construction</h2>
            <p className="text-stone-500 max-w-md">
              L'interface pour la section <span className="text-emerald-400 font-medium">{activeSection}</span> est en cours de développement. 
            </p>
          </div>
        )}
      </main>
    </div>
  );
}

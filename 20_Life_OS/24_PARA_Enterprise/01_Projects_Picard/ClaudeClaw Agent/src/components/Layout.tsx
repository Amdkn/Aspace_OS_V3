import React, { useState } from 'react';
import SideNav from './SideNav';
import AgentStats from './AgentStats';
import Header from './Header';
import RelationDiagram from './RelationDiagram';
import CronsView from './CronsView';
import SkillsView from './SkillsView';
import ScoreCard from './ScoreCard';
import FrameworkOverview from './FrameworkOverview';
import IkigaiPillars from './IkigaiPillars';
import IkigaiHorizons from './IkigaiHorizons';
import LifeWheelDomains from './LifeWheelDomains';
import TwelveWeekYear from './TwelveWeekYear';
import ParaFramework from './ParaFramework';
import GtdFramework from './GtdFramework';
import DealFramework from './DealFramework';
import { motion, AnimatePresence } from 'motion/react';
import { FRAMEWORKS, PEPITES, SIDEBAR_FOOTER } from '../constants';

const Layout: React.FC = () => {
  const [isLeftCollapsed, setIsLeftCollapsed] = useState(true);
  const [isRightCollapsed, setIsRightCollapsed] = useState(true);
  const [activeTab, setActiveTab] = useState('relation');
  const [activeSubItem, setActiveSubItem] = useState<string | null>(null);

  const onNavigate = (id: string, subItem?: string) => {
    setActiveTab(id);
    setActiveSubItem(subItem || null);
  };

  const activeItem = [...FRAMEWORKS, ...PEPITES, ...SIDEBAR_FOOTER].find(item => item.id === activeTab);

  const renderContent = () => {
    switch (activeTab) {
      case 'relation':
        return <RelationDiagram />;
      case 'crons':
        return <CronsView />;
      case 'skills':
        return <SkillsView />;
      case 'scorecard':
        return <ScoreCard />;
    }

    if (activeItem && FRAMEWORKS.some(fw => fw.id === activeTab)) {
      if (activeSubItem) {
        if (activeTab === 'ikigai') {
          const pillarsList = ['Passion', 'Vocation', 'Mission', 'Profession'];
          if (pillarsList.includes(activeSubItem)) {
            return <IkigaiPillars activeSubItem={activeSubItem} />;
          }
          
          const horizonsList = ['SEP:Horizons (Vision)', 'H1 Observer', 'H3 Explorer', 'H10 Guardian', 'H30 Multi-Horizon', 'H90 Cycle Keeper'];
          if (horizonsList.includes(activeSubItem)) {
            return <IkigaiHorizons activeSubItem={activeSubItem} />;
          }
        }

        if (activeTab === 'life-wheel') {
          const domainsList = ['Carrière', 'Finance', 'Santé', 'Croissance', 'Relation', 'Famille', 'Loisir', 'Environnement'];
          if (domainsList.includes(activeSubItem)) {
            return <LifeWheelDomains activeSubItem={activeSubItem} />;
          }
        }

        if (activeTab === '12wy') {
          const twelyList = ['Vision', 'Planning', 'Process Control', 'Measurement', 'Time Use'];
          if (twelyList.includes(activeSubItem)) {
            return <TwelveWeekYear activeSubItem={activeSubItem} />;
          }
        }

        if (activeTab === 'para') {
          const paraList = ['Projects', 'Areas', 'Resources', 'Archive'];
          if (paraList.includes(activeSubItem)) {
            return <ParaFramework activeSubItem={activeSubItem} />;
          }
        }

        if (activeTab === 'gtd') {
          const gtdList = ['Capture', 'Clarify', 'Organize', 'Reflect', 'Engage'];
          if (gtdList.includes(activeSubItem)) {
            return <GtdFramework activeSubItem={activeSubItem} />;
          }
        }

        if (activeTab === 'deal') {
          const dealList = ['Definition', 'Elimination', 'Automation', 'Liberation'];
          if (dealList.includes(activeSubItem)) {
            return <DealFramework activeSubItem={activeSubItem} />;
          }
        }

        return (
          <div className="h-full flex flex-col items-center justify-center p-12 text-center overflow-y-auto">
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="glass-card p-12 max-w-lg border-brass shadow-2xl"
            >
              <h2 className="text-4xl font-black text-white uppercase italic tracking-tighter mb-4 opacity-10">
                {activeSubItem}
              </h2>
              <div className="w-24 h-24 rounded-3xl bg-[var(--glass-l2-bg)] border border-[var(--glass-border)] border-dashed mx-auto mb-8 flex items-center justify-center opacity-40">
                <span className="text-4xl font-bold">🚧</span>
              </div>
              <h3 className="text-xl font-bold text-white uppercase tracking-widest mb-4">Autonomous Vault Initializing</h3>
              <p className="text-sm text-[var(--text-muted)] leading-relaxed italic">
                Scanning IndexedDB / ASpace_OS_V2 for {activeSubItem} telemetry...
                <br/>
                <span className="text-[10px] uppercase font-black text-[var(--accent-warning)] tracking-widest mt-4 block">
                  Integration pending under "The Watcher" protocols.
                </span>
              </p>
            </motion.div>
          </div>
        );
      }
      return <FrameworkOverview data={activeItem as any} />;
    }

    return (
      <div className="h-full flex flex-col items-center justify-center p-12 text-center overflow-y-auto">
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="glass-card p-12 max-w-lg border-brass shadow-2xl"
            >
              <h2 className="text-4xl font-black text-white uppercase italic tracking-tighter mb-4 opacity-10">
                {activeItem?.label}
              </h2>
              <div className="w-24 h-24 rounded-3xl bg-[var(--glass-l2-bg)] border border-[var(--glass-border)] border-dashed mx-auto mb-8 flex items-center justify-center opacity-40">
                <span className="text-4xl font-bold">🚧</span>
              </div>
              <h3 className="text-xl font-bold text-white uppercase tracking-widest mb-4">Autonomous Vault Initializing</h3>
              <p className="text-sm text-[var(--text-muted)] leading-relaxed italic">
                Scanning IndexedDB / ASpace_OS_V2 for {activeItem?.label} telemetry...
                <br/>
                <span className="text-[10px] uppercase font-black text-[var(--accent-warning)] tracking-widest mt-4 block">
                  Integration pending under "The Watcher" protocols.
                </span>
              </p>
            </motion.div>
          </div>
        );
  };

  return (
    <div className="flex h-screen bg-[#020617] overflow-hidden selection:bg-[var(--brass)] selection:text-black">
      {/* Left Sidebar: Frameworks */}
      <SideNav 
        isCollapsed={isLeftCollapsed} 
        onToggle={() => setIsLeftCollapsed(!isLeftCollapsed)} 
        activeId={activeTab}
        onNavigate={onNavigate}
      />
      
      {/* Main Content Area */}
      <main className="flex-1 flex flex-col min-w-0 relative">
        <Header activeId={activeTab} onNavigate={onNavigate} />
        
        <div className="flex-1 overflow-hidden relative">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--glass-bg-hover)_0%,_transparent_70%)] pointer-events-none" />
          
          <AnimatePresence mode="wait">
            <motion.div
              key={`${activeTab}-${activeSubItem || 'overview'}`}
              initial={{ opacity: 0, y: 10, filter: 'blur(10px)' }}
              animate={{ opacity: 1, y: 0, filter: 'blur(0)' }}
              exit={{ opacity: 0, y: -10, filter: 'blur(10px)' }}
              transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
              className="h-full relative z-0 custom-scrollbar overflow-y-auto"
            >
              {renderContent()}
            </motion.div>
          </AnimatePresence>
        </div>
      </main>

      {/* Right IA Panel: Armada */}
      <AgentStats 
        isCollapsed={isRightCollapsed} 
        onToggle={() => setIsRightCollapsed(!isRightCollapsed)} 
      />
    </div>
  );
};

export default Layout;

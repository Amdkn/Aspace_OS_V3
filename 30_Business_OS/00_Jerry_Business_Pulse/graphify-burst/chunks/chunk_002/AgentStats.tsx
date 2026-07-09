import React, { useState } from 'react';
import { ARMADA_FOLDERS, type ArmadaFolder, type Agent } from '../constants';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { 
  PanelRightClose, 
  PanelRightOpen, 
  Cpu, 
  ShieldCheck, 
  ChevronDown, 
  ChevronRight, 
  ArrowLeft,
  Bot,
  Send,
  User,
  Zap,
  Shield
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface AgentStatsProps {
  isCollapsed: boolean;
  onToggle: () => void;
}

const AgentCard: React.FC<{ 
  agent: Agent, 
  isCollapsed: boolean, 
  compact?: boolean,
  onSelect?: (agent: Agent) => void 
}> = ({ agent, isCollapsed, compact, onSelect }) => {
  return (
    <div 
      onClick={() => onSelect?.(agent)}
      className={cn(
        "glass-card p-3 flex flex-col gap-1 hover:bg-[var(--glass-bg-hover)] transition-all cursor-pointer group mb-1",
        isCollapsed ? "items-center px-1" : "px-3",
        compact && "py-2 bg-white/[0.02]"
      )}
    >
      <div className="flex items-center justify-between w-full">
        <div className="flex items-center gap-2">
          {!isCollapsed && (
            <span className={cn(
              "text-xs font-bold text-white group-hover:text-[var(--brass)] transition-colors",
              compact && "text-[10px]"
            )}>
              {agent.name}
            </span>
          )}
          {isCollapsed && (
            <div className={cn(
              "w-8 h-8 rounded-lg flex items-center justify-center bg-[#020617] text-[10px] border border-[var(--glass-border)]",
              agent.status === 'Active' ? "border-[var(--accent-primary)] text-[var(--accent-primary)]" : "border-[var(--text-muted)] text-[var(--text-muted)]"
            )}>
              {agent.name.charAt(0)}
            </div>
          )}
        </div>
        {!isCollapsed && (
          <div className={cn(
            "px-1.5 py-0.5 rounded text-[8px] font-black uppercase tracking-widest",
            agent.status === 'Active' ? "bg-[var(--accent-primary-glow)] text-[var(--accent-primary)]" : "bg-white/5 text-[var(--text-muted)]"
          )}>
            {agent.status}
          </div>
        )}
      </div>
      {!isCollapsed && agent.role && (
        <div className={cn(
          "text-[9px] text-[var(--text-muted)] font-medium leading-tight",
          compact && "text-[8px] opacity-70"
        )}>
          {agent.role}
        </div>
      )}
    </div>
  );
};

const ArmadaFolderAccordion: React.FC<{ 
  folder: ArmadaFolder, 
  isCollapsed: boolean,
  onSelectAgent: (agent: Agent) => void
}> = ({ folder, isCollapsed, onSelectAgent }) => {
  const [isOpen, setIsOpen] = useState(folder.id === 'a0');
  const Icon = folder.icon;

  if (isCollapsed) {
    return (
      <div className="w-8 h-8 rounded-lg flex items-center justify-center bg-[#020617] border border-[var(--glass-border)] text-[var(--brass)] mx-auto mb-2 group relative">
        <Icon className="w-4 h-4" />
        <div className="absolute left-full ml-2 px-2 py-1 bg-black text-[8px] font-bold rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap z-50 pointer-events-none border border-[var(--glass-border)]">
          {folder.label}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-1">
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className={cn(
          "w-full glass-card p-3 flex items-center justify-between hover:bg-[var(--glass-bg-hover)] transition-all group",
          folder.id.startsWith('a0') && "border-brass shadow-[0_0_15px_rgba(184,134,11,0.1)]",
          folder.id.includes('a1') && "bg-white/[0.03]"
        )}
      >
        <div className="flex-1 flex items-center gap-2">
          {isOpen ? <ChevronDown className="w-3 h-3 text-[var(--brass)]" /> : <ChevronRight className="w-3 h-3 text-[var(--text-muted)]" />}
          <Icon className={cn("w-4 h-4", folder.status === 'Active' ? "text-[var(--accent-primary)]" : "text-[var(--brass)]")} />
          <span className={cn(
            "text-xs font-black uppercase tracking-tighter group-hover:text-[var(--brass)] leading-none",
            folder.id === 'a0' && "text-[var(--accent-primary)]"
          )}>
            {folder.label}
          </span>
        </div>
        <div className={cn(
          "px-1.5 py-0.5 rounded text-[8px] font-black uppercase tracking-widest",
          folder.status === 'Active' ? "text-[var(--accent-primary)]" : "text-[var(--text-muted)]"
        )}>
          {folder.status}
        </div>
      </button>
      
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="overflow-hidden pl-4 space-y-1 border-l border-[var(--glass-border-subtle)] ml-2 mb-2"
          >
            {folder.agents.map((agent) => (
              <AgentCard 
                key={agent.name} 
                agent={agent} 
                isCollapsed={isCollapsed} 
                compact 
                onSelect={onSelectAgent}
              />
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

const AgentChatView: React.FC<{ agent: Agent, onBack: () => void }> = ({ agent, onBack }) => {
  const mockMessages = [
    { id: 1, role: 'system', content: `Uplink established with Unit: ${agent.name.split(' ')[0].toUpperCase()}.` },
    { id: 2, role: 'agent', content: `Overseer, this is ${agent.name}. My current status is ${agent.status.toLowerCase()}. System protocols initialized for specialized ${agent.role} deployment.` },
    { id: 3, role: 'agent', content: `Awaiting specific domain instructions. How can I assist with the current framework lifecycle?` },
  ];

  return (
    <motion.div 
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      className="flex flex-col h-full overflow-hidden"
    >
      {/* Agent Info Header in Chat */}
      <div className="px-4 py-3 bg-[var(--glass-l2-bg)] border-b border-[var(--glass-border-subtle)] flex items-center gap-3">
        <div className="w-10 h-10 rounded-full border border-[var(--brass)]/30 bg-[var(--brass)]/5 flex items-center justify-center relative">
          <User className="w-5 h-5 text-[var(--brass)]" />
          <div className="absolute bottom-0 right-0 w-2.5 h-2.5 rounded-full bg-[var(--accent-primary)] border-2 border-[var(--surface-desktop)] shadow-[0_0_5px_var(--accent-primary)]" />
        </div>
        <div>
          <h4 className="text-[10px] font-black text-white uppercase tracking-widest leading-none mb-1">{agent.name}</h4>
          <p className="text-[8px] text-[var(--text-muted)] italic leading-none">{agent.role}</p>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar">
        {mockMessages.map((msg) => (
          <div 
            key={msg.id} 
            className={cn(
              "flex flex-col gap-1.5",
              msg.role === 'system' ? "items-center" : "items-start"
            )}
          >
            {msg.role === 'system' ? (
              <div className="px-2 py-0.5 rounded-full bg-[var(--glass-l2-bg)] border border-[var(--glass-border-subtle)] text-[7px] font-black uppercase text-[var(--text-muted)] tracking-[0.2em]">
                {msg.content}
              </div>
            ) : (
              <div className="flex gap-2 max-w-[95%] group">
                <div className="w-6 h-6 rounded bg-[var(--brass)]/10 border border-[var(--brass)]/30 flex items-center justify-center shrink-0">
                  <Bot className="w-3.5 h-3.5 text-[var(--brass)]" />
                </div>
                <div className="glass-card bg-[var(--glass-l2-bg)] px-3 py-2 rounded-xl rounded-tl-none border border-[var(--glass-border-subtle)] group-hover:border-[var(--brass)]/20 transition-colors">
                  <p className="text-[10px] text-[var(--text-secondary)] leading-relaxed italic">
                    {msg.content}
                  </p>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Input Field */}
      <div className="p-4 border-t border-[var(--glass-border-subtle)] bg-[var(--glass-l2-bg)]">
        <div className="relative group">
          <input 
            type="text" 
            placeholder={`Instruct ${agent.name.split(' ')[0]}...`} 
            className="w-full bg-[var(--glass-bg)] border border-[var(--glass-border-subtle)] rounded-lg px-3 py-2 text-[10px] text-white placeholder-[var(--text-muted)] focus:outline-none focus:border-[var(--brass)]/40 transition-all group-hover:bg-[var(--glass-bg-hover)]"
          />
          <button className="absolute right-2 top-1/2 -translate-y-1/2 p-1 rounded bg-[var(--brass)]/10 text-[var(--brass)] hover:bg-[var(--brass)]/20 transition-colors border border-[var(--brass)]/20">
            <Send className="w-3 h-3" />
          </button>
        </div>
        <div className="flex items-center gap-3 mt-3 px-1 opacity-50">
          <div className="flex items-center gap-1">
            <Shield className="w-2.5 h-2.5 text-[var(--brass)]" />
            <span className="text-[7px] font-black text-white uppercase tracking-widest">Secured</span>
          </div>
          <div className="flex items-center gap-1">
            <Zap className="w-2.5 h-2.5 text-[var(--accent-primary)]" />
            <span className="text-[7px] font-black text-white uppercase tracking-widest">Real-time</span>
          </div>
        </div>
      </div>
    </motion.div>
  );
};

const AgentStats: React.FC<AgentStatsProps> = ({ isCollapsed, onToggle }) => {
  const [activeAgent, setActiveAgent] = useState<Agent | null>(null);

  const handleSelectAgent = (agent: Agent) => {
    if (isCollapsed) return; // Don't switch to chat if collapsed (though icons aren't clickable)
    setActiveAgent(agent);
  };

  return (
    <aside 
      className={cn(
        "h-screen glass border-l border-[var(--glass-border)] flex flex-col transition-all duration-300 relative z-20",
        isCollapsed ? "w-[72px]" : "w-[300px]"
      )}
    >
      <div className="h-[var(--header-height)] flex items-center px-4 border-b border-[var(--glass-border-subtle)] gap-2">
        <button 
          onClick={onToggle}
          className="p-2 rounded-lg hover:bg-[var(--glass-bg-hover)] text-[var(--text-muted)] hover:text-white transition-colors shrink-0"
        >
          {isCollapsed ? <PanelRightOpen className="w-5 h-5" /> : <PanelRightClose className="w-5 h-5" />}
        </button>
        
        {!isCollapsed && (
          <div className="flex-1 flex items-center justify-between overflow-hidden">
            {activeAgent ? (
              <button 
                onClick={() => setActiveAgent(null)}
                className="flex items-center gap-2 group hover:text-[var(--brass)] transition-colors"
              >
                <ArrowLeft className="w-3 h-3 text-[var(--brass)] group-hover:-translate-x-0.5 transition-transform" />
                <span className="text-[10px] font-black tracking-widest text-[var(--brass)] uppercase truncate">Back to Armada</span>
              </button>
            ) : (
              <div className="flex items-center gap-2 overflow-hidden truncate">
                <span className="text-[10px] font-black tracking-[.2em] text-[var(--accent-primary)] uppercase">Armada Telemetry</span>
                <div className="w-2 h-2 rounded-full bg-[var(--accent-primary)] animate-pulse shadow-[0_0_5px_var(--accent-primary)] shrink-0" />
              </div>
            )}
          </div>
        )}
      </div>

      <div className="flex-1 overflow-hidden relative">
        <AnimatePresence mode="wait">
          {activeAgent && !isCollapsed ? (
            <AgentChatView 
              key="chat"
              agent={activeAgent} 
              onBack={() => setActiveAgent(null)} 
            />
          ) : (
            <motion.div 
              key="list"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="h-full p-4 space-y-6 overflow-y-auto custom-scrollbar"
            >
              {/* A0 Sovereign Folder */}
              <div className="space-y-2">
                {ARMADA_FOLDERS.filter(f => f.id === 'a0').map((folder) => (
                  <ArmadaFolderAccordion 
                    key={folder.id} 
                    folder={folder} 
                    isCollapsed={isCollapsed} 
                    onSelectAgent={handleSelectAgent}
                  />
                ))}
              </div>

              {!isCollapsed && (
                <div className="h-px bg-gradient-to-r from-transparent via-[var(--glass-border)] to-transparent opacity-20" />
              )}

              {/* L1 Gatekeepers Group */}
              <div className={cn(
                "space-y-2",
                !isCollapsed && "p-2 rounded-xl border border-brass/30 bg-brass/[0.02] shadow-[inset_0_0_20px_rgba(184,134,11,0.05)]"
              )}>
                {!isCollapsed && (
                  <div className="px-2 mb-1 flex items-center justify-between">
                    <span className="text-[9px] font-black text-brass uppercase tracking-[0.2em] opacity-60">L1 Gatekeepers</span>
                  </div>
                )}
                {ARMADA_FOLDERS.filter(f => f.id.includes('a1')).map((folder) => (
                  <ArmadaFolderAccordion 
                    key={folder.id} 
                    folder={folder} 
                    isCollapsed={isCollapsed} 
                    onSelectAgent={handleSelectAgent}
                  />
                ))}
              </div>

              {/* L2 Starships Group */}
              <div className={cn(
                "space-y-2",
                !isCollapsed && "p-2 rounded-xl border border-brass/20 bg-white/[0.01] shadow-[0_4px_20px_rgba(0,0,0,0.2)]"
              )}>
                {!isCollapsed && (
                  <div className="px-2 mb-1 flex items-center justify-between">
                    <span className="text-[9px] font-black text-brass uppercase tracking-[0.2em] opacity-60">L2 Starships</span>
                  </div>
                )}
                {ARMADA_FOLDERS.filter(f => f.id.includes('a2')).map((folder) => (
                  <ArmadaFolderAccordion 
                    key={folder.id} 
                    folder={folder} 
                    isCollapsed={isCollapsed} 
                    onSelectAgent={handleSelectAgent}
                  />
                ))}
              </div>

              {!isCollapsed && (
                <div className="pt-6 border-t border-[var(--glass-border-subtle)] space-y-4">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <Cpu className="w-4 h-4 text-[var(--brass)]" />
                      <span className="text-[10px] font-black text-white uppercase tracking-widest">L1 Sovereign Node</span>
                    </div>
                    <span className="text-[10px] font-mono text-[var(--brass)]">0xBMAD</span>
                  </div>
                  
                  <div className="grid grid-cols-2 gap-3">
                    <div className="glass-card p-2 text-center">
                      <div className="text-[10px] text-[var(--text-muted)] uppercase mb-1">Load</div>
                      <div className="text-sm font-black text-white">12%</div>
                    </div>
                    <div className="glass-card p-2 text-center">
                      <div className="text-[10px] text-[var(--text-muted)] uppercase mb-1">Status</div>
                      <div className="text-sm font-black text-[var(--accent-primary)] font-mono">OK</div>
                    </div>
                  </div>
                </div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      <div className="p-4 border-t border-[var(--glass-border-subtle)] bg-[var(--glass-l2-bg)] text-center">
        {!isCollapsed ? (
          <div className="flex items-center justify-center gap-2">
            <ShieldCheck className="w-4 h-4 text-[var(--brass)]" />
            <span className="text-[9px] font-bold text-white uppercase tracking-widest">Beth Veto Active</span>
          </div>
        ) : (
          <ShieldCheck className="w-4 h-4 text-[var(--brass)] mx-auto" />
        )}
      </div>
    </aside>
  );
};

export default AgentStats;

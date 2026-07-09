import React from 'react';
import { motion } from 'motion/react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { Layout, CheckCircle2, Clock, Eye, AlertCircle, MoreHorizontal } from 'lucide-react';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface Task {
  id: string;
  title: string;
  status: 'todo' | 'in-progress' | 'review' | 'done';
  steps: string[];
  activeStep: number;
  label: string;
}

const MOCK_TASKS: Task[] = [
  {
    id: 'D-001',
    title: 'Build agent setup for [REDACTED]',
    status: 'todo',
    steps: ['PLAN', 'BUILD', 'TEST', 'DEPLOY'],
    activeStep: 0,
    label: '[REDACTED]'
  },
  {
    id: 'D-002',
    title: 'Configure Slack integration for [REDACTED]',
    status: 'todo',
    steps: ['PLAN', 'BUILD', 'TEST', 'DEPLOY'],
    activeStep: 0,
    label: '[REDACTED]'
  },
  {
    id: 'D-005',
    title: 'Deploy CRM automation agent for [REDACTED]',
    status: 'in-progress',
    steps: ['PLAN', 'BUILD', 'TEST', 'DEPLOY'],
    activeStep: 1,
    label: '[REDACTED]'
  },
  {
    id: 'D-007',
    title: 'Train support agent on [REDACTED] knowledge base',
    status: 'in-progress',
    steps: ['PREP', 'TRAIN', 'VALIDATE', 'SHIP'],
    activeStep: 1,
    label: '[REDACTED]'
  },
  {
    id: 'D-006',
    title: 'Add webhook retry logic to agent runtime',
    status: 'review',
    steps: ['PLAN', 'BUILD', 'TEST', 'REDEPLOY'],
    activeStep: 2,
    label: 'Platform'
  },
  {
    id: 'D-010',
    title: 'Deliver onboarding agent to [REDACTED]',
    status: 'done',
    steps: ['PLAN', 'BUILD', 'TEST', 'DEPLOY'],
    activeStep: 3,
    label: '[REDACTED]'
  },
  {
    id: 'D-011',
    title: 'Set up staging environment',
    status: 'done',
    steps: ['PLAN', 'DO', 'REVIEW', 'DONE'],
    activeStep: 3,
    label: 'Internal'
  }
];

const ScoreCard: React.FC = () => {
  const columns = [
    { id: 'todo', label: 'TODO', icon: Layout, color: 'text-slate-400', bg: 'bg-slate-400' },
    { id: 'in-progress', label: 'IN PROGRESS', icon: Clock, color: 'text-amber-500', bg: 'bg-amber-500' },
    { id: 'review', label: 'REVIEW', icon: Eye, color: 'text-blue-500', bg: 'bg-blue-500' },
    { id: 'done', label: 'DONE', icon: CheckCircle2, color: 'text-emerald-500', bg: 'bg-emerald-500' }
  ];

  const stats = {
    done: MOCK_TASKS.filter(t => t.status === 'done').length,
    review: MOCK_TASKS.filter(t => t.status === 'review').length,
    inProgress: MOCK_TASKS.filter(t => t.status === 'in-progress').length,
    todo: MOCK_TASKS.filter(t => t.status === 'todo').length,
    total: MOCK_TASKS.length
  };

  const percentComplete = Math.round((stats.done / stats.total) * 100);

  return (
    <div className="h-full flex flex-col p-8 pb-0 overflow-hidden">
      {/* Header Section */}
      <div className="flex justify-between items-start mb-8">
        <div>
          <h1 className="text-4xl font-black text-white italic tracking-tighter uppercase mb-1">
            Sprint — <span className="text-[var(--brass)] px-2">Wk13</span>
          </h1>
          <p className="text-[10px] text-[var(--text-muted)] font-black uppercase tracking-[0.3em] mb-4">
            Mar 24 — Mar 28, 2026
          </p>
          <p className="text-xs text-[var(--text-secondary)] italic opacity-60">
            Agent deployments, client integrations, internal tooling
          </p>
        </div>
        
        <div className="text-right">
          <div className="text-4xl font-black text-white italic leading-none">5</div>
          <div className="text-[10px] text-[var(--text-muted)] font-black uppercase tracking-widest mt-1">days left</div>
        </div>
      </div>

      {/* Metrics Bar */}
      <div className="mb-12">
        <div className="flex justify-between text-[10px] font-black uppercase tracking-widest mb-3">
          <div className="flex gap-4">
            <span className="text-emerald-500 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 shadow-[0_0_5px_emerald]" />
              {stats.done} done
            </span>
            <span className="text-blue-500 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-blue-500 shadow-[0_0_5px_blue]" />
              {stats.review} review
            </span>
            <span className="text-amber-500 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-amber-500 shadow-[0_0_5px_amber]" />
              {stats.inProgress} in progress
            </span>
            <span className="text-slate-400 flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-slate-400" />
              {stats.todo} todo
            </span>
          </div>
          <div className="text-[var(--text-muted)] italic">
            {percentComplete}% complete
          </div>
        </div>
        
        <div className="h-1.5 w-full bg-[var(--glass-l2-bg)] rounded-full overflow-hidden flex gap-0.5">
          <div className="bg-emerald-500 h-full shadow-[0_0_10px_rgba(16,185,129,0.3)]" style={{ width: `${(stats.done/stats.total)*100}%` }} />
          <div className="bg-blue-500 h-full shadow-[0_0_10px_rgba(59,130,246,0.3)]" style={{ width: `${(stats.review/stats.total)*100}%` }} />
          <div className="bg-amber-500 h-full shadow-[0_0_10px_rgba(245,158,11,0.3)]" style={{ width: `${(stats.inProgress/stats.total)*100}%` }} />
          <div className="bg-slate-700 h-full" style={{ width: `${(stats.todo/stats.total)*100}%` }} />
        </div>
      </div>

      {/* Kanban Board */}
      <div className="flex-1 grid grid-cols-4 gap-6 overflow-hidden min-h-0">
        {columns.map((col) => (
          <div key={col.id} className="flex flex-col min-h-0">
            <div className="flex items-center justify-between mb-4 px-2">
              <div className="flex items-center gap-2">
                <div className={cn("w-1.5 h-1.5 rounded-full", col.bg)} />
                <h3 className="text-[11px] font-black text-white tracking-[0.2em] uppercase">{col.label}</h3>
              </div>
              <span className="w-5 h-5 rounded-full bg-[var(--glass-l2-bg)] flex items-center justify-center text-[10px] font-black text-[var(--text-muted)]">
                {MOCK_TASKS.filter(t => t.status === col.id).length}
              </span>
            </div>

            <div className="flex-1 overflow-y-auto custom-scrollbar space-y-4 pr-2 pb-8">
              {MOCK_TASKS.filter(t => t.status === col.id).map((task) => (
                <motion.div
                  key={task.id}
                  whileHover={{ y: -2, scale: 1.01 }}
                  className="glass-card p-4 border border-[var(--glass-border-subtle)] relative group cursor-pointer hover:border-[var(--glass-border)] transition-all duration-300"
                >
                  <div className="flex justify-between items-start mb-3">
                    <span className="text-[9px] font-black text-[var(--text-muted)] uppercase tracking-widest">{task.id}</span>
                    <MoreHorizontal className="w-3.5 h-3.5 text-[var(--text-muted)] opacity-0 group-hover:opacity-100 transition-opacity" />
                  </div>
                  
                  <h4 className="text-[13px] font-bold text-white leading-tight mb-4 group-hover:text-[var(--brass)] transition-colors">
                    {task.title}
                  </h4>

                  <div className="grid grid-cols-4 gap-1 mb-3">
                    {task.steps.map((step, idx) => (
                      <div 
                        key={step} 
                        className={cn(
                          "h-4 rounded-[4px] flex items-center justify-center text-[7px] font-black tracking-tighter uppercase",
                          idx <= task.activeStep 
                            ? "bg-emerald-500/20 text-emerald-400 border border-emerald-500/30" 
                            : "bg-[var(--glass-bg)] text-[var(--text-muted)] border border-[var(--glass-border-subtle)]"
                        )}
                      >
                        {step}
                      </div>
                    ))}
                  </div>

                  <div className="flex items-center gap-2">
                    <div className={cn(
                      "px-2 py-0.5 rounded text-[8px] font-black uppercase tracking-widest",
                      task.label.includes('REDACTED') 
                        ? "bg-amber-500/10 text-amber-500/80" 
                        : "bg-blue-500/10 text-blue-500/80"
                    )}>
                      {task.label}
                    </div>
                  </div>
                  
                  {/* Subtle progress indicator */}
                  {col.id === 'in-progress' && (
                    <div className="absolute bottom-0 left-0 h-[1px] bg-[var(--accent-warning)] animate-pulse" style={{ width: '40%' }} />
                  )}
                </motion.div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ScoreCard;

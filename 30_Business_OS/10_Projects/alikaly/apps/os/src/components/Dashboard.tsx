import React from 'react';
import { 
  DollarSign, 
  Target, 
  Clock, 
  AlertTriangle, 
  CheckCircle2, 
  ArrowUpRight, 
  ChevronRight,
  TrendingUp,
  Activity
} from 'lucide-react';
import { Area, AreaChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { cn } from '../lib/utils';
import { motion } from 'motion/react';

const pipelineData = [
  { name: 'W1', value: 45 },
  { name: 'W2', value: 65 },
  { name: 'W3', value: 85 },
  { name: 'W4', value: 70 },
  { name: 'W5', value: 100 },
  { name: 'W6', value: 125 },
];

function StatCard({ title, value, subtext, icon: Icon, trend, isPositive }: any) {
  return (
    <div className="p-5 rounded-xl bg-stone-900 border border-stone-800 flex flex-col gap-4 relative overflow-hidden group hover:border-stone-700 transition-colors">
      <div className="flex justify-between items-start">
        <div className="w-10 h-10 rounded-lg bg-stone-800 flex items-center justify-center border border-stone-700">
          <Icon className="w-5 h-5 text-emerald-500" />
        </div>
        {trend && (
          <div className={cn("flex items-center gap-1 text-xs font-medium px-2 py-1 rounded-full", isPositive ? "text-emerald-400 bg-emerald-500/10" : "text-amber-400 bg-amber-500/10")}>
            {trend} <ArrowUpRight className={cn("w-3 h-3", !isPositive && "rotate-90")} />
          </div>
        )}
      </div>
      <div>
        <h4 className="text-stone-400 text-sm font-medium mb-1">{title}</h4>
        <div className="text-2xl font-display font-semibold text-stone-100">{value}</div>
        {subtext && <p className="text-xs text-stone-500 mt-1">{subtext}</p>}
      </div>
      
      {/* Subtle background glow */}
      <div className="absolute -bottom-6 -right-6 w-24 h-24 bg-emerald-500/5 blur-2xl rounded-full group-hover:bg-emerald-500/10 transition-colors pointer-events-none" />
    </div>
  );
}

function WindDirection() {
  const alerts = [
    {
      id: 1,
      type: 'critical',
      title: 'Motion to Disburse rejetée',
      description: 'Besoin de Probate pour Case #A 2403702',
      time: 'Il y a 2h',
      icon: AlertTriangle
    },
    {
      id: 2,
      type: 'warning',
      title: 'Acompte de 10% à virer',
      description: 'Délai restant : 10 jours ouvrables',
      time: 'Il y a 5h',
      icon: Clock
    },
    {
      id: 3,
      type: 'success',
      title: 'Signature DocuSign',
      description: 'Affidavit of Heirship signé par J. Doe',
      time: 'Hier, 14:30',
      icon: CheckCircle2
    }
  ];

  return (
    <div className="rounded-xl bg-stone-900 border border-stone-800 flex flex-col h-full">
      <div className="p-5 border-b border-stone-800 flex justify-between items-center">
        <div>
          <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
            <Activity className="w-4 h-4 text-emerald-500" />
            Wind Direction
          </h3>
          <p className="text-xs text-stone-500 mt-1">Signaux et actions requises</p>
        </div>
        <button className="text-xs font-medium text-emerald-400 hover:text-emerald-300 transition-colors">
          Voir tout
        </button>
      </div>
      <div className="flex-1 p-5 flex flex-col gap-4">
        {alerts.map((alert) => (
          <div key={alert.id} className="flex gap-4 items-start p-3 rounded-lg hover:bg-stone-800/50 transition-colors cursor-pointer border border-transparent hover:border-stone-800">
            <div className={cn(
              "p-2 rounded-md shrink-0 border",
              alert.type === 'critical' ? 'bg-red-500/10 border-red-500/20 text-red-400' :
              alert.type === 'warning' ? 'bg-amber-500/10 border-amber-500/20 text-amber-400' :
              'bg-emerald-500/10 border-emerald-500/20 text-emerald-400'
            )}>
              <alert.icon className="w-4 h-4" />
            </div>
            <div className="flex-1 min-w-0">
              <h4 className="text-sm font-medium text-stone-200 truncate">{alert.title}</h4>
              <p className="text-xs text-stone-500 mt-0.5 truncate">{alert.description}</p>
            </div>
            <div className="text-xs text-stone-600 whitespace-nowrap">{alert.time}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function PipelineChart() {
  return (
    <div className="rounded-xl bg-stone-900 border border-stone-800 p-5 col-span-1 lg:col-span-2 overflow-hidden flex flex-col min-h-[300px]">
      <div className="mb-6 flex justify-between items-end">
        <div>
          <h3 className="text-sm font-display font-semibold text-stone-100 flex items-center gap-2">
            <TrendingUp className="w-4 h-4 text-emerald-500" />
            Croissance du Pipeline (Commissions Nettes)
          </h3>
          <p className="text-xs text-stone-500 mt-1">Projection sur les 6 dernières semaines</p>
        </div>
        <div className="text-right">
          <div className="text-2xl font-display font-semibold text-emerald-400">$125,000</div>
          <p className="text-xs text-stone-500">Total projeté</p>
        </div>
      </div>
      
      <div className="flex-1 w-full relative">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={pipelineData} margin={{ top: 10, right: 0, left: 0, bottom: 0 }}>
            <defs>
              <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#10b981" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <Tooltip 
              contentStyle={{ backgroundColor: '#1c1917', borderColor: '#292524', borderRadius: '8px' }}
              itemStyle={{ color: '#34d399' }}
              labelStyle={{ color: '#a8a29e' }}
            />
            <Area type="monotone" dataKey="value" stroke="#10b981" strokeWidth={2} fillOpacity={1} fill="url(#colorValue)" />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export function Dashboard() {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="p-8 max-w-7xl mx-auto space-y-8"
    >
      <header className="flex justify-between items-end">
        <div>
          <h1 className="text-2xl font-display font-semibold tracking-tight text-stone-100">Ecosystem Vitals</h1>
          <p className="text-sm text-stone-500 mt-1">Vue d'ensemble de l'écosystème Alykaly</p>
        </div>
        <div className="flex items-center gap-3">
          <span className="text-xs text-emerald-500 flex items-center gap-2 bg-emerald-500/10 px-3 py-1.5 rounded-full font-medium border border-emerald-500/20">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            System nominal
          </span>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard 
          title="Trésorerie MTD" 
          value="$42,500" 
          subtext="Liquidity War Chest"
          icon={DollarSign}
          trend="+12%"
          isPositive={true}
        />
        <StatCard 
          title="Valeur du Pipeline" 
          value="$125k" 
          subtext="25 Alpha Leads (Commissions pot.)"
          icon={Target}
          trend="+5.2%"
          isPositive={true}
        />
        <StatCard 
          title="Taux de Conversion" 
          value="94%" 
          subtext="Target: 95%"
          icon={CheckCircle2}
          trend="-1.5%"
          isPositive={false}
        />
        <StatCard 
          title="Délai Moyen" 
          value="11 sem." 
          subtext="Du sourcing au décaissement"
          icon={Clock}
          trend="-2 sem."
          isPositive={true}
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <PipelineChart />
        <WindDirection />
      </div>
    </motion.div>
  );
}

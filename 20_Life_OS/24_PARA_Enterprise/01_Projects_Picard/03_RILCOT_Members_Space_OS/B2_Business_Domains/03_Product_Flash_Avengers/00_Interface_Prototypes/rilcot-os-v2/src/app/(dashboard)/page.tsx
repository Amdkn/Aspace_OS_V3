"use client";

import React, { useEffect, useState } from 'react';
import { Icons } from '@/components/Icons';
import { useAuth } from '@/contexts/AuthContext';
import Link from 'next/link';
import { dashboardService } from '@/services/dashboardService';
import { toast } from 'sonner';

const MenuGridItem = ({ icon: Icon, label, href, color = "bg-blue-100 text-blue-600" }: { icon: any, label: string, href: string, color?: string }) => (
  <Link 
    href={href}
    className="flex flex-col items-center justify-center p-4 bg-white rounded-2xl shadow-sm hover:shadow-md transition-all active:scale-95 aspect-square"
  >
    <div className={`p-3 rounded-full mb-3 ${color}`}>
      <Icon size={24} />
    </div>
    <span className="text-xs font-medium text-center text-slate-700 leading-tight">{label}</span>
  </Link>
);

const StatCard = ({ label, value, sub, trend, loading }: { label: string, value: string | number, sub?: string, trend?: string, loading?: boolean }) => (
  <div className="bg-white p-4 rounded-2xl shadow-sm border border-slate-100 flex flex-col justify-between h-full">
    <div className="text-sm text-slate-500 mb-1">{label}</div>
    {loading ? (
      <div className="h-8 w-16 bg-slate-100 animate-pulse rounded"></div>
    ) : (
      <div className="text-2xl font-bold text-slate-800">{value}</div>
    )}
    {sub && <div className={`text-xs mt-2 ${trend === 'positive' ? 'text-green-600' : 'text-slate-400'}`}>{sub}</div>}
  </div>
);

export default function DashboardPage() {
  const { session } = useAuth();
  const userName = session?.user?.user_metadata?.full_name || 'Membre';
  const [stats, setStats] = useState({ members: 0, projects: 0, budget: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStats() {
      try {
        const data = await dashboardService.getGlobalStats();
        setStats(data);
      } catch (err) {
        toast.error("Échec du chargement des statistiques en temps réel");
      } finally {
        setLoading(false);
      }
    }
    loadStats();
  }, []);

  return (
    <div className="p-4 space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center mb-2">
        <div className="flex items-center gap-3">
          <img src={`https://api.dicebear.com/7.x/avataaars/svg?seed=${userName}`} alt="Profile" className="w-12 h-12 rounded-full border-2 border-orange-200" />
          <div>
            <h1 className="text-xl font-bold text-slate-900">Bonjour, {userName}!</h1>
            <p className="text-sm text-slate-500">Bienvenue sur RILCOT OS</p>
          </div>
        </div>
        <button onClick={() => toast.info("Aucune nouvelle notification")} className="p-2 text-slate-400 hover:text-slate-600">
          <Icons.Bell size={24} />
        </button>
      </div>

      {/* Quick Stats Widget (Scrollable) */}
      <div className="flex overflow-x-auto gap-4 no-scrollbar pb-2">
        <div className="min-w-[160px]">
          <StatCard label="Membres actifs" value={stats.members.toLocaleString()} sub="+5.2%" trend="positive" loading={loading} />
        </div>
        <div className="min-w-[160px]">
          <StatCard label="Projets en cours" value={stats.projects} sub="+2 ce mois" trend="positive" loading={loading} />
        </div>
        <div className="min-w-[160px]">
          <StatCard label="Budget" value={`${stats.budget}%`} sub="-1.5% vs N-1" loading={loading} />
        </div>
      </div>

      {/* Main Grid Navigation */}
      <div className="grid grid-cols-3 gap-3">
        <MenuGridItem icon={Icons.UserPlus} label="Adhésions" href="/membership" />
        <MenuGridItem icon={Icons.Building} label="Gouvernance" href="/governance" />
        <MenuGridItem icon={Icons.PiggyBank} label="Finances" href="/finance" />
        
        <MenuGridItem icon={Icons.FolderOpen} label="Projets" href="/projects" />
        <MenuGridItem icon={Icons.GraduationCap} label="Réseau Univ." href="/university" />
        <MenuGridItem icon={Icons.Megaphone} label="Recherche" href="#" />
        
        <MenuGridItem icon={Icons.MessageSquare} label="Comms" href="#" />
        <MenuGridItem icon={Icons.Briefcase} label="Talents" href="#" />
        <MenuGridItem icon={Icons.ShieldCheck} label="Qualité" href="#" />
      </div>

      {/* Upcoming Events Teaser */}
      <div>
        <h2 className="text-lg font-bold text-slate-900 mb-3">Événements à venir</h2>
        <div className="bg-white rounded-2xl shadow-sm border border-slate-100 divide-y divide-slate-50">
          <Link href="/calendar" className="w-full p-4 flex items-center justify-between hover:bg-slate-50 text-left">
            <div className="flex items-center gap-4">
              <div className="bg-blue-100 p-2 rounded-lg text-blue-600">
                <Icons.Users size={20} />
              </div>
              <div>
                <div className="font-semibold text-slate-800">Réunion du Conseil</div>
                <div className="text-xs text-slate-500">Aujourd'hui, 14:00 - Virtuel</div>
              </div>
            </div>
            <Icons.ChevronRight size={16} className="text-slate-400" />
          </Link>
           <Link href="/calendar" className="w-full p-4 flex items-center justify-between hover:bg-slate-50 text-left">
            <div className="flex items-center gap-4">
              <div className="bg-orange-100 p-2 rounded-lg text-orange-600">
                <Icons.MapPin size={20} />
              </div>
              <div>
                <div className="font-semibold text-slate-800">Séminaire annuel</div>
                <div className="text-xs text-slate-500">25 Oct, 09:00 - Centre de Congrès</div>
              </div>
            </div>
            <Icons.ChevronRight size={16} className="text-slate-400" />
          </Link>
        </div>
      </div>
    </div>
  );
}

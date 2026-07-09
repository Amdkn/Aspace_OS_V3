"use client";

import { BottomNav } from "@/components/BottomNav";
import ProtectedRoute from "@/components/ProtectedRoute";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-slate-50 max-w-md mx-auto shadow-2xl relative overflow-hidden flex flex-col">
        <main className="flex-1 overflow-y-auto no-scrollbar pb-24">
          {children}
        </main>
        <BottomNav />
      </div>
    </ProtectedRoute>
  );
}

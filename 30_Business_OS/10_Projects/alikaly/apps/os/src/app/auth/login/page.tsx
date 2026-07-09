'use client';

import React, { Suspense, useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { createSupabaseBrowserClient } from '@/lib/supabase/client';

function LoginForm() {
  const router = useRouter();
  const params = useSearchParams();
  const redirect = params.get('redirect') ?? '/';

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const supabase = createSupabaseBrowserClient();
    const { error: signinErr } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    setLoading(false);
    if (signinErr) {
      setError(signinErr.message);
      return;
    }
    router.push(redirect);
    router.refresh();
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="w-full max-w-sm bg-stone-900 border border-stone-800 rounded-2xl p-8 space-y-5"
    >
      <header className="mb-2">
        <h1 className="text-xl font-display font-semibold text-stone-100">
          Alykaly OS — Sovereign Login
        </h1>
        <p className="text-xs text-stone-500 mt-1">
          Investor &amp; Operator Access
        </p>
      </header>

      <label className="block text-sm">
        <span className="text-stone-400">Email</span>
        <input
          type="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="mt-1 w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-stone-200 focus:border-emerald-500 outline-none"
          autoComplete="email"
        />
      </label>

      <label className="block text-sm">
        <span className="text-stone-400">Password</span>
        <input
          type="password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mt-1 w-full bg-stone-950 border border-stone-800 rounded-lg px-3 py-2 text-stone-200 focus:border-emerald-500 outline-none"
          autoComplete="current-password"
        />
      </label>

      {error && (
        <p className="text-xs text-red-400 bg-red-500/10 border border-red-500/20 rounded-lg px-3 py-2">
          {error}
        </p>
      )}

      <button
        type="submit"
        disabled={loading}
        className="w-full bg-emerald-500 hover:bg-emerald-400 disabled:opacity-50 text-stone-950 font-medium rounded-lg py-2 transition"
      >
        {loading ? 'Authenticating…' : 'Enter Sanctum'}
      </button>
    </form>
  );
}

export default function LoginPage() {
  return (
    <div className="min-h-screen bg-stone-950 flex items-center justify-center p-8 text-stone-300">
      <Suspense
        fallback={
          <div className="text-stone-500 text-sm">Loading…</div>
        }
      >
        <LoginForm />
      </Suspense>
    </div>
  );
}

// ============================================================================
// Supabase Admin Client (Server-only, bypasses RLS via service_role)
// USE WITH CARE — never expose this client to the browser.
// ============================================================================
import 'server-only';
import { createClient } from '@supabase/supabase-js';

export function createSupabaseAdminClient() {
  return createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    { auth: { persistSession: false, autoRefreshToken: false } }
  );
}

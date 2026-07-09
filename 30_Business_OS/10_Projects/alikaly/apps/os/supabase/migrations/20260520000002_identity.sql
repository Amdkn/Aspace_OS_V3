-- ============================================================================
-- Alykaly OS — Migration 002
-- Identity : profiles + helpers (current_user_role/clearance/org)
-- ============================================================================

CREATE TABLE identity.profiles (
  user_id           UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  org_id            TEXT NOT NULL DEFAULT 'alykaly',
  display_name      TEXT NOT NULL,
  email             TEXT NOT NULL,
  role              identity.user_role NOT NULL DEFAULT 'viewer',
  clearance         identity.clearance_level NOT NULL DEFAULT 'level_1_internal',
  avatar_url        TEXT,
  preferences       JSONB NOT NULL DEFAULT '{}'::JSONB,
  last_seen_at      TIMESTAMPTZ,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX profiles_org_role_idx   ON identity.profiles(org_id, role);
CREATE INDEX profiles_clearance_idx  ON identity.profiles(clearance);
CREATE INDEX profiles_email_idx      ON identity.profiles(email);

COMMENT ON TABLE identity.profiles IS 'One row per auth.users — extends with role/clearance/org';

-- ===== Trigger : auto-create profile when auth.users INSERT =====
CREATE OR REPLACE FUNCTION identity.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO identity.profiles (user_id, display_name, email)
  VALUES (
    NEW.id,
    COALESCE(NEW.raw_user_meta_data->>'display_name', split_part(NEW.email, '@', 1)),
    NEW.email
  )
  ON CONFLICT (user_id) DO NOTHING;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public, identity, auth;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION identity.handle_new_user();

-- ===== Helpers : RLS-friendly (STABLE + SECURITY DEFINER) =====
CREATE OR REPLACE FUNCTION identity.current_user_clearance()
RETURNS identity.clearance_level
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = identity, public AS $$
  SELECT clearance FROM identity.profiles WHERE user_id = auth.uid();
$$;

CREATE OR REPLACE FUNCTION identity.current_user_role()
RETURNS identity.user_role
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = identity, public AS $$
  SELECT role FROM identity.profiles WHERE user_id = auth.uid();
$$;

CREATE OR REPLACE FUNCTION identity.current_user_org()
RETURNS TEXT
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = identity, public AS $$
  SELECT COALESCE((SELECT org_id FROM identity.profiles WHERE user_id = auth.uid()), 'alykaly');
$$;

CREATE OR REPLACE FUNCTION identity.clearance_at_least(target identity.clearance_level)
RETURNS BOOLEAN
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = identity, public AS $$
  SELECT identity.current_user_clearance() >= target;
$$;

GRANT EXECUTE ON FUNCTION
  identity.current_user_clearance(),
  identity.current_user_role(),
  identity.current_user_org(),
  identity.clearance_at_least(identity.clearance_level)
TO authenticated, anon, service_role;

-- ============================================================================
-- Alykaly OS — Migration 008
-- Storage buckets + policies
-- ============================================================================

-- ===== Buckets =====
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES
  ('documents-private',  'documents-private',  false, 52428800, ARRAY['application/pdf','image/png','image/jpeg','application/zip']),
  ('intake-attachments', 'intake-attachments', false, 20971520, ARRAY['application/pdf','image/png','image/jpeg']),
  ('marketing-public',   'marketing-public',   true,  10485760, NULL)
ON CONFLICT (id) DO NOTHING;

-- ===== documents-private policies =====
CREATE POLICY "documents_private_select_authorized"
ON storage.objects FOR SELECT TO authenticated
USING (
  bucket_id = 'documents-private'
  AND EXISTS (
    SELECT 1 FROM crm.documents d
    WHERE d.bucket = 'documents-private'
      AND d.storage_path = storage.objects.name
      AND d.org_id = identity.current_user_org()
      AND identity.clearance_at_least(d.clearance_required)
      AND d.deleted_at IS NULL
  )
);

CREATE POLICY "documents_private_insert_operator"
ON storage.objects FOR INSERT TO authenticated
WITH CHECK (
  bucket_id = 'documents-private'
  AND identity.current_user_role() IN ('admin','operator','agent')
);

CREATE POLICY "documents_private_delete_admin"
ON storage.objects FOR DELETE TO authenticated
USING (
  bucket_id = 'documents-private'
  AND identity.current_user_role() = 'admin'
);

-- ===== intake-attachments policies =====
CREATE POLICY "intake_attachments_anon_insert"
ON storage.objects FOR INSERT TO anon
WITH CHECK (
  bucket_id = 'intake-attachments'
  AND octet_length(name) < 200
);

CREATE POLICY "intake_attachments_operator_select"
ON storage.objects FOR SELECT TO authenticated
USING (
  bucket_id = 'intake-attachments'
  AND identity.current_user_role() IN ('admin','operator','agent')
);

CREATE POLICY "intake_attachments_admin_delete"
ON storage.objects FOR DELETE TO authenticated
USING (
  bucket_id = 'intake-attachments'
  AND identity.current_user_role() = 'admin'
);

-- ===== marketing-public policies =====
-- Public read is automatic when bucket.public = true.
CREATE POLICY "marketing_public_insert_admin"
ON storage.objects FOR INSERT TO authenticated
WITH CHECK (
  bucket_id = 'marketing-public'
  AND identity.current_user_role() IN ('admin','operator')
);

CREATE POLICY "marketing_public_update_admin"
ON storage.objects FOR UPDATE TO authenticated
USING (
  bucket_id = 'marketing-public'
  AND identity.current_user_role() = 'admin'
);

CREATE POLICY "marketing_public_delete_admin"
ON storage.objects FOR DELETE TO authenticated
USING (
  bucket_id = 'marketing-public'
  AND identity.current_user_role() = 'admin'
);

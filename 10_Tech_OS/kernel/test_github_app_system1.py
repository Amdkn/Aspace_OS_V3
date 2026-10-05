import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[2] / "scripts" / "github_app_system1.py"
SPEC = importlib.util.spec_from_file_location("github_app_system1", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class GitHubAppSystem1Tests(unittest.TestCase):
    def test_all_profiles_validate(self):
        doc = MODULE.load_profiles()
        for name, profile in doc["profiles"].items():
            MODULE.validate(name, doc["defaults"], profile)

    def test_unspecified_permissions_deny_by_default(self):
        _, gateway = MODULE.get_profile("gateway")
        self.assertEqual(MODULE.effective_level("administration", gateway), "none")
        self.assertEqual(MODULE.effective_level("workflows", gateway), "none")
        self.assertEqual(MODULE.effective_level("repository_projects", gateway), "none")

    def test_metadata_is_mandatory_read(self):
        _, s3 = MODULE.get_profile("s3")
        self.assertEqual(MODULE.effective_level("metadata", s3), "read (GitHub mandatory)")

    def test_a0_does_not_request_classic_repository_projects(self):
        _, a0 = MODULE.get_profile("a0")
        self.assertNotIn("repository_projects", a0["permissions"])

    def test_gateway_manifest_has_events_and_no_oauth(self):
        m = MODULE.manifest("gateway")
        self.assertIn("issues", m["default_events"])
        self.assertFalse(m["request_oauth_on_install"])
        self.assertFalse(m["hook_attributes"]["active"])

    def test_a0_manifest_requests_user_authorization(self):
        m = MODULE.manifest("a0")
        self.assertTrue(m["request_oauth_on_install"])
        self.assertIn("callback_urls", m)

    def test_reconcile_computes_current_to_desired_and_marks_widening(self):
        current = {
            "permissions": {
                "metadata": "read",
                "contents": "read",
                "issues": "read",
                "workflows": "write",
            },
            "events": [],
            "request_oauth_on_install": False,
            "webhook_active": False,
        }
        plan = MODULE.reconciliation_plan("s3", current)
        changes = {
            (item.get("kind"), item.get("permission") or item.get("setting")): item
            for item in plan["changes"]
        }
        self.assertEqual(changes[("permission", "contents")]["desired"], "write")
        self.assertEqual(changes[("permission", "contents")]["direction"], "widen")
        self.assertEqual(changes[("permission", "workflows")]["desired"], "none")
        self.assertEqual(changes[("permission", "workflows")]["direction"], "narrow")
        self.assertTrue(plan["contains_permission_widening"])
        self.assertFalse(plan["execution_authorized"])

    def test_reconcile_cannot_authorize_without_explicit_approval(self):
        current = {
            "permissions": {"metadata": "read", "contents": "read"},
            "events": [],
        }
        plan = MODULE.reconciliation_plan("s3", current)
        with self.assertRaises(MODULE.ApprovalRequired):
            MODULE.approve_reconciliation(plan, approved=False)

        approved = MODULE.approve_reconciliation(plan, approved=True)
        self.assertTrue(approved["approved"])
        self.assertTrue(approved["execution_authorized"])

    def test_noop_reconcile_never_authorizes_external_execution(self):
        current = MODULE.desired_state("gateway")
        plan = MODULE.reconciliation_plan("gateway", current)
        self.assertEqual(plan["changes"], [])
        approved = MODULE.approve_reconciliation(plan, approved=False)
        self.assertTrue(approved["approved"])
        self.assertFalse(approved["execution_authorized"])

    def test_unknown_current_permission_fails_closed(self):
        current = {
            "permissions": {
                "metadata": "read",
                "mystery_admin_surface": "admin",
            }
        }
        with self.assertRaises(ValueError):
            MODULE.reconciliation_plan("s3", current)


if __name__ == "__main__":
    unittest.main()

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


if __name__ == "__main__":
    unittest.main()

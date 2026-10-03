import unittest
from cubefarm_ui_primitives import CubeFarmThemeProfile, CubeFarmMultiThemeEngine

class TestCubeFarmUIPrimitives(unittest.TestCase):
    def test_apply_theme_success(self):
        engine = CubeFarmMultiThemeEngine()
        profile = CubeFarmThemeProfile(actor_id="test_actor")
        result = engine.apply_theme(profile, "glass")

        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["active_theme"], "glass")
        self.assertEqual(profile.active_theme, "glass")

    def test_apply_invalid_theme(self):
        engine = CubeFarmMultiThemeEngine()
        profile = CubeFarmThemeProfile(actor_id="test_actor")

        with self.assertRaises(ValueError):
            engine.apply_theme(profile, "invalid_theme_xyz")

if __name__ == "__main__":
    unittest.main()

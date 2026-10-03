"""Tests for CubeFarm Living Office Projections.

Issue #403: Acceptance verification.
"""

import json
import os
import sys
import tempfile
import unittest

# Ensure kernel directory is in path
sys.path.insert(0, os.path.dirname(__file__))

from cubefarm_office import (
    CubeFarmOfficeProjection,
    DeskProjection,
    OfficeFloor,
    RuntimeBody,
)


class TestCubeFarmOffice(unittest.TestCase):

    def test_ryan_desk_renders_identity_embodiment_runtime_workload_separately(self):
        """Acceptance: one live Ryan desk renders identity, embodiment, runtime and workload separately."""
        ryan_desk = DeskProjection(
            actor_id="Ryan",
            hierarchy="S3",
            institutional_state="ACTIVE",
            embodiment_state="EMBODIED",
            workload_state="ACTIVE",
            home="floor_factory_s3",
            missions=["Mission_CubeFarm_Office_403"],
            work_ids=[403],
            effect_leases=["lease_build_factory_01"],
            evidence_head="sha256_ryan_factory_001",
            subagents=["Jules", "Hermes"],
            runtime_bodies=[
                RuntimeBody("Hermes", "ryan", "sess_001", "ACTIVE", "Routing messages"),
                RuntimeBody("Codex", "codex_ryan", "sess_002", "REVIEWING", "Reviewing PR #439"),
                RuntimeBody("Jules", "jules_builder", "sess_003", "BUILDING", "Writing cubefarm_office.py"),
                RuntimeBody("Antigravity", "antigravity_res", "sess_004", "RESEARCHING", "Analyzing holon topology"),
            ],
            return_to="#403",
        )

        rendered = ryan_desk.render_projection()

        self.assertEqual(rendered["schema"], "aspace.desk-projection.v1")

        # 1. Identity section
        identity = rendered["identity"]
        self.assertEqual(identity["value"]["actor_id"], "Ryan")
        self.assertEqual(identity["value"]["hierarchy"], "S3")
        self.assertEqual(identity["value"]["institutional_state"], "ACTIVE")
        self.assertEqual(identity["authority"], "Tech_OS")
        self.assertEqual(identity["source"], "workgraph.identity")

        # 2. Embodiment section
        embodiment = rendered["embodiment"]
        self.assertEqual(embodiment["value"]["embodiment_state"], "EMBODIED")
        self.assertEqual(embodiment["value"]["home"], "floor_factory_s3")
        self.assertEqual(embodiment["value"]["evidence_head"], "sha256_ryan_factory_001")

        # 3. Runtime section (4 concurrent bodies)
        runtime = rendered["runtime"]
        self.assertEqual(runtime["value"]["active_count"], 4)
        runtimes = runtime["value"]["runtime_bodies"]
        harnesses = {r["harness"]: r["runtime_state"] for r in runtimes}
        self.assertEqual(harnesses["Hermes"], "ACTIVE")
        self.assertEqual(harnesses["Codex"], "REVIEWING")
        self.assertEqual(harnesses["Jules"], "BUILDING")
        self.assertEqual(harnesses["Antigravity"], "RESEARCHING")

        # 4. Workload section
        workload = rendered["workload"]
        self.assertEqual(workload["value"]["workload_state"], "ACTIVE")
        self.assertIn("Mission_CubeFarm_Office_403", workload["value"]["missions"])
        self.assertIn(403, workload["value"]["work_ids"])

    def test_switching_runtime_body_preserves_ryan_identity(self):
        """Acceptance: switching runtime body does not recreate/rename Ryan."""
        desk = DeskProjection(
            actor_id="Ryan",
            hierarchy="S3",
            institutional_state="ACTIVE",
            embodiment_state="EMBODIED",
            workload_state="ACTIVE",
            home="floor_factory_s3",
            runtime_bodies=[
                RuntimeBody("Hermes", "ryan", "sess_001", "ACTIVE"),
            ],
        )

        # Switch to Codex & Jules only
        desk.switch_runtime_bodies([
            RuntimeBody("Codex", "codex_ryan", "sess_010", "REVIEWING"),
            RuntimeBody("Jules", "jules_builder", "sess_011", "BUILDING"),
        ])

        self.assertEqual(desk.actor_id, "Ryan")
        self.assertEqual(desk.institutional_state, "ACTIVE")
        self.assertEqual(len(desk.runtime_bodies), 2)
        self.assertEqual(desk.runtime_bodies[0].harness, "Codex")

        # Law 4: Empty/offline runtime does not delete institutional identity
        desk.switch_runtime_bodies([])
        self.assertEqual(desk.actor_id, "Ryan")
        self.assertEqual(desk.institutional_state, "ACTIVE")
        self.assertEqual(len(desk.runtime_bodies), 0)

        rendered = desk.render_projection()
        self.assertEqual(rendered["identity"]["value"]["actor_id"], "Ryan")
        self.assertEqual(rendered["identity"]["value"]["institutional_state"], "ACTIVE")

    def test_non_github_floor_type_rendered_from_anthology(self):
        """Acceptance: one non-GitHub floor type is rendered from Anthology references."""
        floor = OfficeFloor(
            floor_id="floor_life_12wy",
            floor_type="A2 Life framework",
            title="12 Week Year Life Execution Room",
            anthology_refs=[
                "anthology://frameworks/12wy/v1",
                "anthology://holons/a2_river",
            ],
            deep_links={
                "linear": "https://linear.app/aspace/issue/LIFE-12WY",
                "gws": "https://drive.google.com/aspace/12WY_Plan",
                "workgraph": "workgraph://claim/12wy_cycle_01",
            },
        )

        rendered = floor.render_floor_projection()

        self.assertEqual(rendered["floor_type"], "A2 Life framework")
        self.assertEqual(len(rendered["anthology_refs"]), 2)
        ref1 = rendered["anthology_refs"][0]
        self.assertEqual(ref1["value"], "anthology://frameworks/12wy/v1")
        self.assertEqual(ref1["authority"], "Anthology")
        self.assertEqual(ref1["source"], "anthology.registry")

    def test_deep_linking_without_collapsing(self):
        """Acceptance: Office can deep-link to GitHub/Linear/GWS/WorkGraph refs without collapsing them."""
        floor = OfficeFloor(
            floor_id="floor_mission_cell_403",
            floor_type="MissionCell / temporary war-room",
            title="War Room - Issue #403 CubeFarm Office Projection",
            anthology_refs=["anthology://missions/403"],
            deep_links={
                "github": "https://github.com/Amdkn/Aspace_OS_V3/issues/403",
                "linear": "https://linear.app/aspace/issue/TECH-403",
                "gws": "https://drive.google.com/aspace/docs/issue_403_spec",
                "workgraph": "workgraph://task/403_office_projection",
            },
        )

        rendered = floor.render_floor_projection()

        links = rendered["deep_links"]
        self.assertIn("github", links)
        self.assertIn("linear", links)
        self.assertIn("gws", links)
        self.assertIn("workgraph", links)

        self.assertEqual(links["github"]["value"], "https://github.com/Amdkn/Aspace_OS_V3/issues/403")
        self.assertEqual(links["linear"]["value"], "https://linear.app/aspace/issue/TECH-403")
        self.assertEqual(links["gws"]["value"], "https://drive.google.com/aspace/docs/issue_403_spec")
        self.assertEqual(links["workgraph"]["value"], "workgraph://task/403_office_projection")

        # Each remains a distinct deep link with its own source/authority envelope
        self.assertEqual(links["github"]["source"], "deep_link.github")
        self.assertEqual(links["linear"]["source"], "deep_link.linear")

    def test_no_ui_field_silently_becomes_authority(self):
        """Acceptance: no UI field silently becomes authority or SSOT."""
        proj = CubeFarmOfficeProjection()

        floor = OfficeFloor(
            floor_id="floor_b1_enterprise",
            floor_type="B1 business/franchise",
            title="Enterprise B1 Franchise Floor",
            anthology_refs=["anthology://franchises/b1_enterprise"],
        )
        proj.add_floor(floor)

        rendered = proj.render_office_projection()

        self.assertTrue(rendered["is_projection_surface"])
        self.assertIn("projection/runtime surface", rendered["source_of_truth_notice"])

        # Check floor truth projection wrapper
        floor_proj = rendered["floors"][0]
        anthology_proj = floor_proj["anthology_refs"][0]
        self.assertEqual(anthology_proj["truth_state"], "CURRENT")
        self.assertEqual(anthology_proj["authority"], "Anthology")
        self.assertNotEqual(anthology_proj["authority"], "CubeFarm")

    def test_restart_preserves_desk_mission_lineage(self):
        """Acceptance: restart preserves desk/mission lineage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "office_state_test.json")

            office1 = CubeFarmOfficeProjection(storage_filepath=filepath)
            desk_ryan = DeskProjection(
                actor_id="Ryan",
                hierarchy="S3",
                institutional_state="ACTIVE",
                embodiment_state="EMBODIED",
                workload_state="ACTIVE",
                home="floor_factory_s3",
                missions=["Mission_CubeFarm_Office_403"],
                work_ids=[403],
                effect_leases=["lease_factory_01"],
                evidence_head="sha256_head_12345",
                subagents=["Jules"],
                runtime_bodies=[
                    RuntimeBody("Jules", "jules_builder", "sess_builder_99", "BUILDING", "Testing persistence"),
                ],
                return_to="#403",
            )
            floor = OfficeFloor(
                floor_id="floor_factory",
                floor_type="bounded factory floor",
                title="Ryan Factory Floor",
                anthology_refs=["anthology://factories/ryan"],
                desks=[desk_ryan],
                deep_links={"github": "https://github.com/Amdkn/Aspace_OS_V3"},
            )
            office1.add_floor(floor)
            office1.save_office_state()

            # Simulate restart / reload in a new instance
            office2 = CubeFarmOfficeProjection(storage_filepath=filepath)
            loaded_data = office2.load_office_state()

            self.assertEqual(loaded_data["schema"], "aspace.cubefarm-office-state.v1")
            loaded_floor = office2.get_floor("floor_factory")
            self.assertIsNotNone(loaded_floor)
            self.assertEqual(loaded_floor.title, "Ryan Factory Floor")
            self.assertEqual(len(loaded_floor.desks), 1)

            loaded_desk = loaded_floor.desks[0]
            self.assertEqual(loaded_desk.actor_id, "Ryan")
            self.assertEqual(loaded_desk.hierarchy, "S3")
            self.assertEqual(loaded_desk.missions, ["Mission_CubeFarm_Office_403"])
            self.assertEqual(loaded_desk.work_ids, [403])
            self.assertEqual(loaded_desk.return_to, "#403")
            self.assertEqual(loaded_desk.evidence_head, "sha256_head_12345")
            self.assertEqual(len(loaded_desk.runtime_bodies), 1)
            self.assertEqual(loaded_desk.runtime_bodies[0].harness, "Jules")


if __name__ == "__main__":
    unittest.main()

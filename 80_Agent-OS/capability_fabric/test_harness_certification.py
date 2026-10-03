import importlib, unittest
registry_mod=importlib.import_module("80_Agent-OS.capability_fabric.registry")
hlist=importlib.import_module("80_Agent-OS.capability_fabric.harness_list")
inspect=importlib.import_module("80_Agent-OS.capability_fabric.capability_inspect")
adapters=importlib.import_module("80_Agent-OS.capability_fabric.adapters")
cert=importlib.import_module("80_Agent-OS.capability_fabric.harness_certification")

class TestHarnessCertification(unittest.TestCase):
    def setUp(self):
        self.r=registry_mod.CapabilityRegistry()
        hlist.register_harness_list(self.r)
        inspect.register_capability_inspect(self.r)

    def test_certified_harness_uses_shared_capability(self):
        a=adapters.HarnessMeshAdapter(self.r,"hermes")
        res=a.invoke_certified("capability_inspect",{},actor_id="Doctor13",authority_envelope="L2_READ",correlation_id="corr-412")
        self.assertEqual(res["status"],"SUCCESS")
        self.assertEqual(res["certification"]["status"],"PASS")
        self.assertEqual(res["mesh_view"]["identity"]["actor_id"],"Doctor13")

    def test_uncertified_gap_fails_closed(self):
        a=adapters.HarnessMeshAdapter(self.r,"qwen")
        res=a.invoke_certified("capability_inspect",{},actor_id="Doctor13",authority_envelope="L2_READ",correlation_id="corr-gap")
        self.assertEqual(res["status"],"CERTIFICATION_FAILED")

    def test_failover_preserves_identity_and_work(self):
        res=cert.failover_harness(from_harness="hermes",to_harness="codex",actor_id="Ryan",work_id=412,correlation_id="corr-f",authority_envelope="L2_EXECUTE",capability_id="capability_inspect",fail_reason="timeout")
        self.assertEqual(res["actor_id"],"Ryan")
        self.assertEqual(res["work_id"],412)

if __name__=="__main__":
    unittest.main()

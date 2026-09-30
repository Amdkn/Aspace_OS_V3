import os
import sys
import unittest
from pathlib import Path
import re

class TestDCStartup(unittest.TestCase):
    def setUp(self):
        self.ps1_path = Path(__file__).resolve().parent / "dc.ps1"

    def test_startup_script_generation(self):
        """Verifies that launch.cmd is generated using powershell.exe instead of pythonw.exe."""
        content = self.ps1_path.read_text(encoding="utf-8")

        # Check inside Install-DC specifically
        install_func = content.split("function Install-DC {")[1].split("function Start-DC {")[0]
        self.assertNotIn('pythonw.exe', install_func, "Should not use pythonw.exe for launch.cmd generation")
        self.assertIn('$pwsh=(Get-Command powershell.exe).Source', install_func, "Should get powershell.exe path")
        self.assertRegex(install_func, r'-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File', "Should correctly execute the powershell script")

    def test_false_healthy_state_prevention(self):
        """Verifies that Show-Status properly checks for dead supervisor and unavailable health_urls."""
        content = self.ps1_path.read_text(encoding="utf-8")

        self.assertIn('if(-not (Test-Pid ([int]$m.supervisor_pid))){ return [pscustomobject]@{schema="aspace.dc.control.v1";state="STOPPED";reason="SUPERVISOR_DEAD"} }', content, "Should return STOPPED if supervisor is dead")
        self.assertIn('if($health[$h.Name].aggregate -eq "UNAVAILABLE"){ $healthOk=$false }', content, "Should invalidate health if aggregate is UNAVAILABLE")
        self.assertIn('$core=($healthOk) -and $services.m0.alive', content, "Should ensure all health endpoints are ok before setting core to true")

if __name__ == '__main__':
    unittest.main()

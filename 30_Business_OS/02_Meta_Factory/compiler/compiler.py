import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any, Optional
import hashlib

@dataclass
class FranchiseCompileError(Exception):
    msg: str

def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise FranchiseCompileError(f"Invalid JSON at {path}: {e}")
    except FileNotFoundError:
        raise FranchiseCompileError(f"File not found: {path}")

def generate_hash(content: dict) -> str:
    content_str = json.dumps(content, sort_keys=True)
    return hashlib.sha256(content_str.encode('utf-8')).hexdigest()

def compile_franchise(profile: dict, tenant_id: str) -> dict:
    # Based on the contract in issue 281:
    # TenantProfile + BrandProfile + OfferCatalog + WorkflowProfile + SOPBundle + PolicyBundle + EntitlementProfile + DeploymentProfile → Operable Product Instance
    # Semantic contracts come from PSS/UDM/CCS/WER/TPE/RID
    # Overrides are explicit, typed and bounded

    # We create a fully operable product instance manifest here

    version = "1.0.0"

    profiles = {
        "tenant_profile": profile.get("mode", "Standard Tenant"),
        "brand_profile": profile.get("name", "Unnamed Franchise"),
        "offer_catalog": "Standard Engine Offerings",
        "workflow_profile": "Standard Engine",
        "sop_bundle": "Standard SOPs",
        "policy_bundle": "Standard Policies",
        "entitlement_profile": profile.get("parent", "J01_Jerry_Prime_LD01_Business"),
        "deployment_profile": "Coach OS V3 Template"
    }

    # Bounded overrides
    overrides = {
        "focus": {}
    }

    # If the profile specifies a matrix with a focus, extract it as an override
    matrix = profile.get("b2_b3_harmonization_matrix", {})
    for tier, data in matrix.items():
        if "focus" in data:
            overrides["focus"][tier] = data["focus"]

    compiled = {
        "schema": "aspace.business-os.franchise-instance.v1",
        "tenant_id": tenant_id,
        "version": version,
        "semantic_contracts": ["PSS", "UDM", "CCS", "WER", "TPE", "RID"],
        "profiles": profiles,
        "overrides": overrides,
        "b2_b3_harmonization_matrix": matrix,
        "status": profile.get("status", "ACTIVE"),
        "data_ownership": {
            "tenant_id": tenant_id,
            "type": "explicit",
            "storage": "isolated"
        }
    }

    # Build release evidence records configuration version
    compiled["release_evidence"] = {
        "version": version,
        "config_hash": generate_hash(compiled)
    }

    return compiled

def main():
    if len(sys.argv) != 3:
        print("Usage: compiler.py <franchise.json> <output.json>")
        sys.exit(1)

    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    try:
        profile = load_json(in_path)
        tenant_id = profile.get("id") or in_path.stem

        compiled = compile_franchise(profile, tenant_id)

        with out_path.open("w", encoding="utf-8") as f:
            json.dump(compiled, f, indent=2)

        print(f"Compiled {in_path} to {out_path}")
        sys.exit(0)
    except FranchiseCompileError as e:
        print(f"Compilation failed: {e.msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()

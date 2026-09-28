#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PATH = ROOT / "ASPACE_WORKSPACE_REGISTRY.json"


def main() -> int:
    r = json.loads(PATH.read_text(encoding="utf-8"))
    r["updated_at"] = "2026-09-28"
    r["system"]["world_model"] = (
        "Astra=unified A'Space V3; Sol=Agent OS; "
        "Terra=Life OS 2026; Luna=Business federation"
    )

    gh = r["fabrics"]["github"]
    gh["forge_chain"] = "deprecated_fixed_chain"
    gh["forge_model"] = (
        "fractal mission composition: capabilities are reentrant; "
        "Clara compiles topology; Nardole routes throughout"
    )

    sat = r["repositories"]["satellites"]
    sat["agent_os"]["authority"] = "sol_world_parent"
    sat["agent_os"]["legacy_local_junction"] = sat["agent_os"].get("local_junction")
    sat["agent_os"]["local_junction"] = "C:/Users/amado/ASpace_OS_V3/Worlds/Sol"
    sat["agent_os_desktop"]["authority"] = "sol_world_desktop"
    sat["agent_os_desktop"]["local_head"] = "7c6dc8b"
    sat["life_os_2026"]["authority"] = "terra_world"
    sat["life_os_2026"]["legacy_local_junction"] = sat["life_os_2026"].get("local_junction")
    sat["life_os_2026"]["local_junction"] = "C:/Users/amado/ASpace_OS_V3/Worlds/Terra"

    biz = r["repositories"]["business"]
    local = {
        "business_os": "C:/Users/amado/BusinessOS_analysis",
        "business_office_3_os": "C:/Users/amado/Business-Office-3-OS",
        "omk_business_os": "C:/Users/amado/ASpace_Worlds/_repos/01-OMK-Business-OS",
        "omk_mobile_back_office": "C:/Users/amado/The-OMK-Mobile-Back-Office",
        "omk_saas_os": "C:/Users/amado/00-omk-saas-os",
    }
    for key, path in local.items():
        biz[key]["local_path"] = path
        biz[key]["authority"] = "luna_business_federation"

    biz["omk_desktop_web_os"]["authority"] = "luna_business_projection"
    biz["omk_saas_os"]["repo"] = "omk-services/00-omk-saas-os"
    biz["omk_saas_os"]["clone_url"] = "https://github.com/omk-services/00-omk-saas-os.git"
    biz["omk_office_jaas"] = {
        "repo": "Amdkn/The-OMK-Office1.0-JaaS",
        "clone_url": "https://github.com/Amdkn/The-OMK-Office1.0-JaaS.git",
        "default_branch": "main",
        "local_path": "C:/Users/amado/ASpace_Worlds/_repos/The-OMK-Office1.0-JaaS",
        "codespace_path": "business/The-OMK-Office1.0-JaaS",
        "bootstrap": "auto",
        "authority": "luna_business_product",
        "evidence": "GitHub verified",
    }
    biz["omk_landing"] = {
        "repo": "Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web",
        "clone_url": "https://github.com/Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web.git",
        "default_branch": "main",
        "local_path": "C:/Users/amado/The-OMK-Office-V1-JaaS-Landing-Site-Web",
        "codespace_path": "business/The-OMK-Office-V1-JaaS-Landing-Site-Web",
        "bootstrap": "auto",
        "authority": "luna_business_projection",
        "evidence": "GitHub verified",
    }

    r["worlds"] = {
        "Astra": {
            "role": "unified_aspace_v3_system_world",
            "repo": "Amdkn/Aspace_OS_V3",
            "local_path": "C:/Users/amado/ASpace_OS_V3",
            "external_alias": "C:/Users/amado/ASpace_Worlds/Astra",
            "codespace_path": "/workspaces/aspace/worlds/Astra",
            "authority": "A0-Amadeus / Rick's Verse",
        },
        "Sol": {
            "role": "agent_os_interface_and_observability_world",
            "local_path": "C:/Users/amado/agent-os",
            "external_alias": "C:/Users/amado/ASpace_Worlds/Sol",
            "local_junction": "C:/Users/amado/ASpace_OS_V3/Worlds/Sol",
            "codespace_path": "/workspaces/aspace/worlds/Sol",
            "manager_core": "Doctor13",
            "desktop": {
                "repo": "Amdkn/Agent-OS-Desktop",
                "local_path": "C:/Users/amado/agent-os/desktop",
                "port": 5555,
                "host": "127.0.0.1",
                "current_local_head": "7c6dc8b",
            },
        },
        "Terra": {
            "role": "life_os_2026_world",
            "repo": "Amdkn/Life-OS-2026",
            "local_path": "C:/Users/amado/ASpace_Worlds/Life_OS_2026",
            "external_alias": "C:/Users/amado/ASpace_Worlds/Terra",
            "local_junction": "C:/Users/amado/ASpace_OS_V3/Worlds/Terra",
            "codespace_path": "/workspaces/aspace/worlds/Terra",
            "manager_core": "Doctor11",
        },
        "Luna": {
            "role": "business_os_the_omk_office_federation",
            "repo": None,
            "local_path": "C:/Users/amado/ASpace_Worlds/Luna",
            "local_junction": "C:/Users/amado/ASpace_OS_V3/Worlds/Luna",
            "codespace_path": "/workspaces/aspace/worlds/Luna",
            "manager_core": "Doctor12",
            "composition": (
                "junction/symlink federation; member repositories keep "
                "independent Git history"
            ),
            "repositories": [
                spec["repo"] for spec in biz.values() if spec.get("repo")
            ],
        },
    }

    r["relationships"]["local"] = {
        "Astra_to_Sol": {
            "type": "junction",
            "path": "C:/Users/amado/ASpace_OS_V3/Worlds/Sol",
            "target": "C:/Users/amado/agent-os",
            "direction": "mount",
        },
        "Astra_to_Terra": {
            "type": "junction",
            "path": "C:/Users/amado/ASpace_OS_V3/Worlds/Terra",
            "target": "C:/Users/amado/ASpace_Worlds/Life_OS_2026",
            "direction": "mount",
        },
        "Astra_to_Luna": {
            "type": "junction",
            "path": "C:/Users/amado/ASpace_OS_V3/Worlds/Luna",
            "target": "C:/Users/amado/ASpace_Worlds/Luna",
            "direction": "mount",
        },
        "compatibility_aliases": {
            "Agent_OS": {
                "path": "C:/Users/amado/ASpace_OS_V3/Agent_OS",
                "target": "C:/Users/amado/agent-os",
            },
            "Life_OS_2026": {
                "path": "C:/Users/amado/ASpace_OS_V3/Life_OS_2026",
                "target": "C:/Users/amado/ASpace_Worlds/Life_OS_2026",
            },
        },
    }

    r["relationships"]["codespace"] = {
        "world_aliases": {
            "Astra": "core/Aspace_OS_V3",
            "Terra": "satellites/Life-OS-2026",
        },
        "composed_worlds": {
            "Sol": {
                "components": {
                    "Desktop": "satellites/Agent-OS-Desktop",
                    "HermesWorkspace": "satellites/Hermes-Workspace",
                },
                "local_only": {
                    "AgentOSParent": "C:/Users/amado/agent-os",
                    "Observatoire": "C:/Users/amado/agent-os/observatoire",
                },
            },
            "Luna": {
                "components": {
                    "BusinessOS": "business/BusinessOS",
                    "BusinessOffice3OS": "business/Business-Office-3-OS",
                    "OMKBusinessOS": "business/01-OMK-Business-OS",
                    "OMKOfficeJaaS": "business/The-OMK-Office1.0-JaaS",
                    "OMKMobile": "business/The-OMK-Mobile-Back-Office",
                    "OMKDesktop": "business/OMK-DESKTOP-WEB-OS",
                    "OMKSaaS": "business/00-omk-saas-os",
                    "OMKLanding": "business/The-OMK-Office-V1-JaaS-Landing-Site-Web",
                }
            },
        },
        "rule": (
            "World links are filesystem projections over independent Git "
            "repositories; no link changes repository ownership or history."
        ),
    }

    PATH.write_text(
        json.dumps(r, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"UPDATED {PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

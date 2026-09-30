import sqlite3
from typing import Dict, Any

class RoryReconciler:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def reconcile(
        self,
        work_id: int,
        local_runtime_state: Dict[str, Any],
        git_fingerprint: str,
        supabase_projection: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Idempotent reconciliation between four truth planes:
        1. Local runtime state
        2. Local uc.db (work table)
        3. Git / source fingerprint
        4. Supabase aspace projection
        """
        db_status = 'UNKNOWN'

        # Connect to uc.db to get the local WorkGraph truth
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            row = conn.execute("SELECT status FROM work WHERE id = ?", (work_id,)).fetchone()
            if row:
                db_status = row[0]
        except sqlite3.OperationalError:
            # If the DB doesn't exist or doesn't have the table, we handle it gracefully
            pass
        finally:
            if conn:
                conn.close()

        runtime_status = local_runtime_state.get('status', 'UNKNOWN')
        supa_status = supabase_projection.get('status', 'UNKNOWN')

        # Check for nested repo drift from git_fingerprint.
        # Suppose git_fingerprint format could contain something like "DIRTY_AGENT_OS_DESKTOP"
        # or we accept it as part of the state object. For simplicity, we just parse the string.
        nested_repo_drift = False
        if "agentOsDesktopIsDirty=true" in git_fingerprint or "NESTED_REPO_DRIFT" in git_fingerprint:
            nested_repo_drift = True
        elif isinstance(local_runtime_state.get('git'), dict) and local_runtime_state['git'].get('agentOsDesktopIsDirty'):
            nested_repo_drift = True

        # Determine coherence state
        if nested_repo_drift:
            state = 'NESTED_REPO_DRIFT'
            reason = 'Agent OS Desktop nested repo is dirty or diverged.'
            blocker = 'Git drift'
            next_action = 'Commit or reset nested repo changes before reconciliation.'
        elif runtime_status == db_status == supa_status and runtime_status != 'UNKNOWN':
            state = 'COHERENT'
            reason = 'All truth planes match.'
            blocker = None
            next_action = 'No action required.'
        elif runtime_status == db_status and runtime_status != supa_status:
            state = 'DRIFT'
            reason = 'Supabase projection out of sync with local truth.'
            blocker = 'Sync discrepancy'
            next_action = 'Update Supabase projection to match local WorkGraph.'
        elif runtime_status != db_status:
            state = 'CONFLICT'
            reason = 'Runtime state conflicts with local database.'
            blocker = 'Local state divergence'
            next_action = 'Investigate runtime vs DB conflict.'
        else:
            state = 'AMBIGUOUS'
            reason = 'Unresolvable state divergence or missing unprovable data.'
            blocker = 'Missing evidence'
            next_action = 'Require human review or additional evidence.'

        # Create the specific evidence receipt required by the memory directive
        receipt = {
            'work_id': work_id,
            'session_id': local_runtime_state.get('session_id', 'UNKNOWN'),
            'state': state,
            'evidence': {
                'planes': {
                    'runtime': runtime_status,
                    'uc.db': db_status,
                    'supabase': supa_status
                },
                'git_fingerprint': git_fingerprint,
                'reason': reason
            },
            'blocker': blocker,
            'next_action': next_action
        }
        return receipt

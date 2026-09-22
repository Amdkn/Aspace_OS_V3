1. **Create LM Studio Registry Module**
   - Create directory `10_Tech_OS/kernel/slm/lm_studio`.
   - Create `lm_studio_registry.py` inside it.
   - Implement `LMStudioRegistry` class.
   - Implement methods for: `discover_models`, `health_check`, `estimate_resources`, `load_model`, `unload_model`, and `enforce_ttl_policy`.
   - Ensure to use Python's standard `urllib.request` for REST API interactions as specified.

2. **Create Unit Tests**
   - Create `test_lm_studio_registry.py` in the same directory.
   - Mock `urllib.request.urlopen` to test API interactions (e.g., successful/failed discovery, health check).
   - Test TTL policy enforcement logic.
   - Test load/unload state updates.
   - Use `unittest` module to match other Kernel tests.

3. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
   - Call `pre_commit_instructions` tool.
   - Run tests `PYTHONPATH=$(pwd)/10_Tech_OS/kernel python3 -m unittest discover -s 10_Tech_OS/kernel/ -p 'test_*.py'`.

4. **Submit PR**
   - Commit the changes with branch name `AUTO_CREATE_PR`.
   - Submit the task.

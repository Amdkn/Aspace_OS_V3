1. **Create Discovery Corpus Module**: In `30_Business_OS/10_Research_Atlas/02_Discovery_Corpus/discovery_corpus.py`.
   - Implement `extract_citations` to find DOI, arXiv, etc., in descriptions.
   - Implement `resolve_paper` to mock paper resolution for citations.
   - Implement `analyze_transcript` to generate structured analysis of claims/methods.
   - Implement `process_video` that orchestrates:
     a. Fetching basic metadata/transcript.
     b. Calling `watch.capture_video` for frame extraction & base packet.
     c. Enhancing the packet with canonical papers and transcript analysis.
     d. Generating PaperGraph edges.
   - Implement `process_corpus` to iterate over a manifest of videos.

2. **Create Tests**: In `30_Business_OS/10_Research_Atlas/02_Discovery_Corpus/test_discovery_corpus.py`.
   - Use mocks to simulate `watch.capture_video`, network calls, etc. for deterministic CI.
   - Add a live canary test that processes a short video, skipped if network/tools unavailable.

3. **Pre-commit**: Complete pre-commit steps to make sure proper testing, verifications, reviews and reflections are done.

4. **Submit**: Create a PR referencing #207 and #240.

# Bill WATCH S1 Video Microscope

WATCH is Bill's S1 microscope for a selected video, converting a single source into a structured evidence packet.
It is explicitly NOT the historical harvester or Discover AI corpus generation.

## Capture Pipeline
`source -> transcript -> metadata -> keyframes -> repository/code refs -> evidence packet`

## Usage

```bash
python3 watch.py <youtube_url> --out-dir <output_directory>
```

This will output:
1. `metadata.json`
2. Transcripts (e.g., `.vtt` files)
3. Keyframes in `frames/`
4. `evidence_packet.json` (The final output referencing the generated artifacts and code refs)

## Testing
Run unit tests with:
```bash
python3 test_watch.py
```

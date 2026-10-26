"""Pre-generated overlay store.

PLANNED (Phase 4): after document upload, background-generate "standard"
overlays for every chunk and cache by (chunk_id, level, detail). Live
requests check cache first to drop display latency below 1s.

Not implemented in MVP.
"""

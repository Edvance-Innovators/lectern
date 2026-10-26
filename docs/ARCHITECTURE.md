# Architecture

- **Document ingestion** -> parsed into chunks (backend/parser.py)
- **Overlay generation** -> LLM + level/detail prompts (backend/generator.py)
- **Presenter UI** -> select chunk, choose level, generate, push (frontend/)
- **Audience view** -> polls /latest, renders Markdown (frontend/audience.html)

Phase 3 adds live STT (backend/stt/) and concept matching
(backend/matching/). Phase 4 adds overlay caching (backend/cache/).

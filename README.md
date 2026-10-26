# lectern

Live presentation overlays grounded in your own documents.

Upload a PDF/DOCX/PPTX, select any passage, and generate a teaching
slide at primary, secondary, university, or public-talk level.

**Status:** MVP - manual selection working. Live speech-to-text
planned (see `docs/ROADMAP.md`).

## Quickstart

    git clone https://github.com/<you>/lectern
    cd lectern
    cp .env.example .env      # add your OPENAI_API_KEY
    make install
    make run

- Presenter: http://localhost:8000/index.html
- Audience:  http://localhost:8000/audience.html

## How it works

1. Upload a document -> parsed into paragraph-level chunks
2. Click a chunk -> choose audience level + detail depth
3. LLM generates a Markdown overlay slide
4. Push to audience window (second monitor / projector)

## Roadmap

- [x] Document parsing (PDF/DOCX/PPTX)
- [x] Manual chunk selection + overlay generation
- [x] Level-aware prompts (primary -> public talk)
- [x] Audience projection view
- [ ] Live speech-to-text with concept matching
- [ ] Overlay caching for instant display
- [ ] MathJax rendering for equations

See `docs/ROADMAP.md` for details.

## License

MIT - see `LICENSE`.

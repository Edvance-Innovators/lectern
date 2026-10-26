"""FastAPI app: upload, generate, push, latest."""
import shutil
import uuid
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.parser import parse_document
from backend.generator import generate_overlay
from backend.models import GenerateRequest, PushRequest
from backend.session import SESSIONS, LATEST_OVERLAY

app = FastAPI(title="lectern")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOADS = Path("uploads")
UPLOADS.mkdir(exist_ok=True)


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    session_id = str(uuid.uuid4())[:8]
    dest = UPLOADS / f"{session_id}_{file.filename}"
    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    try:
        chunks = parse_document(str(dest))
    except Exception as e:
        raise HTTPException(400, f"Parse failed: {e}")
    if not chunks:
        raise HTTPException(400, "No text extracted")
    SESSIONS[session_id] = {"chunks": chunks, "filename": file.filename}
    return {
        "session_id": session_id,
        "filename": file.filename,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }


@app.post("/generate")
async def generate(req: GenerateRequest):
    session = SESSIONS.get(req.session_id)
    if not session:
        raise HTTPException(404, "Session not found")
    chunk = next((c for c in session["chunks"] if c["id"] == req.chunk_id), None)
    if not chunk:
        raise HTTPException(404, "Chunk not found")
    if req.level not in {"primary", "secondary", "university", "public"}:
        raise HTTPException(400, "Invalid level")
    if req.detail not in {"brief", "standard", "deep"}:
        raise HTTPException(400, "Invalid detail")
    try:
        md = generate_overlay(chunk["text"], req.level, req.detail)
    except Exception as e:
        raise HTTPException(500, f"Generation failed: {e}")
    return {"markdown": md}


@app.post("/push")
async def push(req: PushRequest):
    LATEST_OVERLAY["markdown"] = req.markdown
    return {"ok": True}


@app.get("/latest")
async def latest():
    return LATEST_OVERLAY


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

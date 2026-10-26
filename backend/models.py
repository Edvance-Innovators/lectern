"""Pydantic request/response models."""
from pydantic import BaseModel
from typing import Optional


class Chunk(BaseModel):
    id: str
    text: str
    page: Optional[int] = None
    type: str = "paragraph"


class GenerateRequest(BaseModel):
    session_id: str
    chunk_id: str
    level: str = "university"
    detail: str = "standard"


class PushRequest(BaseModel):
    markdown: str

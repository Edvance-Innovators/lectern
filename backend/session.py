"""In-memory session store. MVP only - swap to SQLite/Redis before real use."""
SESSIONS: dict[str, dict] = {}
LATEST_OVERLAY: dict = {"markdown": "# Waiting for overlay..."}

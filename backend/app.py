# backend/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel
from typing import Optional, Dict, Any
from pathlib import Path
import os
import requests
import base64
import io

# ---- Local imports
from utils.config import settings
from models.recommender import ContentRecommender


# =========================
# Paths & Config (robust)
# =========================
BASE_DIR = Path(__file__).parent.resolve()

# Data path: prefer settings.DATA_PATH if valid, else default to ./data/products.csv
_data_path = Path(getattr(settings, "DATA_PATH", "") or "")
if not (_data_path and _data_path.exists()):
    _data_path = BASE_DIR / "data" / "products.csv"

# Vector index dir: prefer settings.VECTOR_INDEX_DIR if set, else ./vectorstore
_vector_dir = Path(getattr(settings, "VECTOR_INDEX_DIR", "") or (BASE_DIR / "vectorstore"))
_vector_dir.mkdir(parents=True, exist_ok=True)

# Embedding model name from settings (required by your code)
_model_name = getattr(settings, "EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")

# Frontend build directory (React/Vite "dist")
# - You can override with env FRONTEND_DIST if you want
FRONTEND_DIST = Path(os.getenv("FRONTEND_DIST", BASE_DIR / "frontend_dist")).resolve()


# =========================
# App & Middleware
# =========================
app = FastAPI(title="Ikarus (UI + API)", version="1.0")

# With single-host deployment CORS is typically unnecessary, but harmless to leave open
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten to your domain if you want
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Lazy init of recommender
# =========================
reco: Optional[ContentRecommender] = None

@app.on_event("startup")
def _startup():
    global reco
    # Instantiate once app starts (keeps import-time light and avoids path issues during build)
    reco = ContentRecommender(
        data_path=_data_path,
        vector_index_dir=_vector_dir,
        embedding_model_name=_model_name,
    )


# =========================
# API Models
# =========================
class RecommendReq(BaseModel):
    prompt: str
    top_k: int = 6
    filters: Optional[Dict[str, Any]] = None


# =========================
# API Routes (all under /api)
# =========================
@app.get("/api/ping")
def ping():
    return {"ok": True, "data_path": str(_data_path), "vector_dir": str(_vector_dir)}

@app.post("/api/recommend")
def recommend(req: RecommendReq):
    items = reco.recommend(req.prompt, req.top_k, req.filters or {})
    return {"items": items}

@app.get("/api/item/{uniq_id}")
def item(uniq_id: str):
    return reco.item(uniq_id)

@app.get("/api/analytics")
def analytics():
    return reco.analytics()

@app.get("/api/proxy-image")
def proxy_image(url: str):
    """
    Fetch external image server-side to avoid hotlink/CORS/mixed-content issues.
    Returns transparent 1x1 PNG on failure.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, stream=True, timeout=10, headers=headers)
        r.raise_for_status()
        ctype = r.headers.get("content-type", "image/jpeg")
        return StreamingResponse(r.raw, media_type=ctype)
    except Exception:
        transparent_png = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWP4//8/AwAI/AL+qsg7xQAAAABJRU5ErkJggg=="
        )
        return StreamingResponse(io.BytesIO(transparent_png), media_type="image/png")


# =========================
# Serve React build (single URL)
# =========================
# Build step should copy frontend/dist/* to backend/frontend_dist/
# See deploy section: cp -r frontend/dist/* backend/frontend_dist/
if FRONTEND_DIST.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="frontend")
else:
    # If the build isn't present, expose a simple hint at root.
    # (Your API remains available at /api/* regardless.)
    @app.get("/")
    def root_hint():
        return {
            "message": "Frontend bundle not found. Build your frontend and copy dist/ to backend/frontend_dist/",
            "expected_dir": str(FRONTEND_DIST),
            "api_docs": "/docs",
            "api_base": "/api",
        }

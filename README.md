# 🛒 Ikarus – Product Recommendation System

A full-stack AI/ML-powered **product recommendation platform**, built with:

- **FastAPI** (backend API)
- **React/Vite** (frontend UI)
- **ML embeddings** (for similarity-based product recommendations)

---

## ✨ Features
- 🔍 Content-based product recommendations  
- 📊 Analytics endpoint for category/brand/price insights  
- 🖼 Image proxy endpoint to safely load external product images  
- 🖥 React frontend served directly by FastAPI (single deployment, no CORS issues)  
- ⚡ Deployable on **Render** / **Railway** in one click  

---

## 📂 Project Structure
ikarus_rec_app/
├─ backend/
│ ├─ app.py # FastAPI entrypoint
│ ├─ data/
│ │ └─ products.csv # Raw dataset
│ ├─ models/
│ │ └─ recommender.py # Recommendation engine
│ ├─ utils/
│ │ └─ config.py # Settings (paths, embedding model, etc.)
│ └─ requirements.txt # Python dependencies
├─ frontend/ # React/Vite frontend
└─ README.md


---

## 🚀 Getting Started (Local Development)

### 1. Clone the repo
```bash
git clone https://github.com/PreetKundi/IKARUS-AI_ML-ASSIGNMENT.git
cd IKARUS-AI_ML-ASSIGNMENT

### BACKEND
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

Run the backend:
uvicorn backend.app:app --reload --port 8000

3. Frontend setup
cd ../frontend
npm install
npm run dev

Tech Stack

Backend: FastAPI, Uvicorn, Pandas, NumPy

Frontend: React, Vite, Tailwind (optional)

Deployment: Render (free tier)

ML: Embedding model (configurable in utils/config.py)

services:
  - type: web
    name: ikarus
    env: python
    plan: free
    buildCommand: |
      pip install -r backend/requirements.txt
      cd frontend && npm ci && npm run build && cd ..
      rm -rf backend/frontend_dist
      mkdir -p backend/frontend_dist
      cp -r frontend/dist/* backend/frontend_dist/
    startCommand: uvicorn backend.app:app --host 0.0.0.0 --port $PORT



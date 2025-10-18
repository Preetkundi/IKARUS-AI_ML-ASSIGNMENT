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
```text
ikarus_rec_app/
├─ backend/
│  ├─ app.py                # FastAPI entrypoint
│  ├─ data/
│  │  └─ products.csv       # Raw dataset
│  ├─ models/
│  │  └─ recommender.py     # Recommendation engine
│  ├─ utils/
│  │  └─ config.py          # Settings (paths, embedding model, etc.)
│  └─ requirements.txt      # Python dependencies
├─ frontend/                # React/Vite frontend
└─ README.md


---

## 🚀 Getting Started (Local Development)

### 1. Clone the repo
```bash
git clone https://github.com/PreetKundi/IKARUS-AI_ML-ASSIGNMENT.git
cd IKARUS-AI_ML-ASSIGNMENT


### 2. Backend setup
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt

      



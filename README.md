# 🛒 Ikarus – Product Recommendation System

Ikarus is a full-stack **AI/ML-powered product recommendation platform**.  
It provides **personalized recommendations** using embeddings, analytics for pricing/brands, and a frontend that integrates seamlessly with the backend.  

The system is designed to mimic **real-world e-commerce recommendation engines**, combining **data preprocessing, ML embeddings, and a React frontend**.

---

## ✨ Key Features
- 🔍 **Content-based recommendations** using text embeddings  
- 📊 **Analytics endpoints**: price distribution, brand/category trends  
- 🖼 **Image proxy API**: safely serve product images without CORS issues  
- 🖥 **React + Vite frontend** served directly by FastAPI (single deployment)  
- ⚡ **Deployable on Render** with one click (backend + frontend together)  

---

## 📂 Project Structure
```text
ikarus_rec_app/
├─ backend/
│  ├─ app.py                # FastAPI entrypoint
│  ├─ data/
│  │  ├─ products.csv       # Raw dataset
│  │  └─ products_clean.csv # Preprocessed dataset
│  ├─ models/
│  │  └─ recommender.py     # Content-based recommendation engine
│  ├─ utils/
│  │  └─ config.py          # Settings (paths, embedding model, etc.)
│  └─ requirements.txt      # Python dependencies
├─ frontend/                # React/Vite frontend
└─ README.md

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
```

## 🛠 Tech Stack (Detailed)

The project integrates **Machine Learning, NLP, Computer Vision, Generative AI, and a full-stack deployment pipeline**.  
Below is the detailed breakdown of each layer and why it was chosen:

---

### 🔹 Backend
- **FastAPI** → Chosen for its speed, async support, and automatic OpenAPI documentation (`/docs`).  
- **Uvicorn** → ASGI server to run the FastAPI app in production.  
- **Pandas / NumPy** → For preprocessing, cleaning, and analytics on product data.  
- **Scikit-learn** → Used for lightweight ML (recommendation logic, clustering, text processing if needed).  

---

### 🔹 NLP (Natural Language Processing)
- **Hugging Face Transformers (SentenceTransformers)** → For generating text embeddings (`all-MiniLM-L6-v2`), enabling semantic similarity search.  
- **spaCy** (optional) → For text preprocessing like lemmatization and entity extraction.  

Why embeddings?  
They allow us to compare **user queries vs. product descriptions** in vector space → enabling **content-based recommendations**.

---

### 🔹 CV (Computer Vision)
- **CNN / Vision Transformers (ViT/ResNet)** → Used for image-based embeddings 
- These models help classify product images into categories (e.g., shoes, shirts) and improve recommendation accuracy.  

---

### 🔹 Generative AI (GenAI)
- **Lightweight GenAI models (e.g., GPT-2 / DistilGPT, or OpenAI/Groq APIs if available)**  
- Used to generate **creative product descriptions** and enrich recommendations.  
- Example: If a product has missing metadata, the model can generate a marketing-friendly description.  

---

### 🔹 Vector Database
- **FAISS ** → Used in this project to index and search embeddings efficiently.  


Why vector DB?  
Embeddings are high-dimensional vectors → we need a fast similarity search engine for real-time recommendations.

---

### 🎨 Frontend
- **React + Vite** → Lightweight, modern frontend setup with fast dev server and build optimization.  
- **TailwindCSS** (optional) → For clean, responsive UI styling with minimal boilerplate.  
- **Axios / Fetch API** → For communicating with FastAPI backend (`/api` endpoints).  

Frontend Responsibilities:
- Take user prompt (e.g., *“red running shoes under $100”*)  
- Send request to backend `/api/recommend`  
- Display recommended products + analytics  

---

### 📊 Analytics
- **Matplotlib / Seaborn** → For data visualization (price distribution, top brands, categories).  
- **Pandas Profiling ** → For EDA on dataset.  
- **React Charts (Recharts, Chart.js)** → For rendering analytics charts on the frontend.  

---

### ☁️ Deployment
- **Render** → Chosen for simplicity, allows serving both backend + frontend in one service.  




---
## ▶️ How to Run This Project

Follow these steps to run the **Ikarus Product Recommendation System** locally:

---

### 1. Clone the repository
```bash
git clone https://github.com/PreetKundi/IKARUS-AI_ML-ASSIGNMENT.git
cd IKARUS-AI_ML-ASSIGNMENT
```

### 2. Setup and run the Backend (FastAPI)
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```
Run the backend:
```bash
uvicorn app:app --reload --port 8000
```

### 3. Setup and run the Frontend (React + Vite)
```bash
cd ../frontend
npm install
npm run dev
```

4. Using the Application

Open the frontend in your browser → http://127.0.0.1:5173

Enter a query (e.g., "red running shoes")

The app will call the backend /api/recommend endpoint and show recommended products.

Use /api/analytics or the frontend analytics page to view product trends, price distribution, and top categories.




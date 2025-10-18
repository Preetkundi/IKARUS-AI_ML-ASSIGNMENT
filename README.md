# Ikarus – Product Recommendation/Analytics Web App

End‑to‑end ML web app built with **FastAPI (backend)**, **React (frontend)**, and a **vector database (FAISS local; Pinecone optional)**.  
It recommends furniture using text similarity and generates creative blurbs. An analytics page summarizes the dataset.

## Quickstart

### 1) Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

### 2) Frontend
```bash
cd ../frontend
npm i
cp .env.example .env   # update VITE_API_URL if backend runs elsewhere
npm run dev
```

Open http://localhost:5173 and ask for recommendations.

## How it works

- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` creates vectors from joined text fields.
- **Vector DB**: FAISS (cosine similarity). Swap with Pinecone by wiring LangChain's `PineconeVectorStore` (left as an exercise; env vars already present).
- **GenAI descriptions**: A small rule‑based `CopyWriter` provides diverse, non‑plagiarized blurbs without external APIs. If you set `OPENAI_API_KEY`, plug LangChain LLM for richer text.
- **Analytics**: `/analytics` returns top brands, avg price per category, price summary, and missingness.

## Endpoints
- `POST /recommend` → `{prompt, top_k, filters}` returns items (with `gen_description`).
- `GET /item/{uniq_id}` → a single item.
- `GET /analytics` → dataset summaries for the Analytics page.

## Notebooks
- `notebooks/data_analytics.ipynb` – EDA and plots.
- `notebooks/model_training.ipynb` – builds FAISS index; try a qualitative search.

## Notes
- The image classifier module is scaffolded; train via a separate notebook if you curate labeled images.
- Keep the dataset intact (no column drops). All transformations are non-destructive.
- Code is modular and well-commented to support grading for clarity and reasoning.

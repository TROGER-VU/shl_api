# 🧠 SHL Product Recommendation API

This API provides intelligent recommendations for SHL assessments based on user queries using a Retrieval-Augmented Generation (RAG) approach. It uses semantic search over vector embeddings generated from SHL product descriptions.

---

## 🚀 Live Demos

- 🔍 **Streamlit Demo App** (User-facing search interface): [https://shl-troger.streamlit.app/](https://shl-troger.streamlit.app/)
- 🔗 **API Endpoint** (FastAPI): [https://shl-api-ut7j.onrender.com](https://shl-api-ut7j.onrender.com)
  - Interactive docs: [https://shl-api-ut7j.onrender.com/docs](https://shl-api-ut7j.onrender.com/docs)

---

## 🧰 Tech Stack

- **FastAPI** – for backend API.
- **Streamlit** – for frontend demo.
- **Sentence Transformers** – for embedding queries and SHL products.
- **Supabase** – as a vector database backend.
- **Uvicorn** – as the ASGI server.

---

## 📦 Installation (For Local Setup)

```bash
git clone https://github.com/your-username/shl-recommendation-api
cd shl-recommendation-api
pip install -r requirements.txt
```

---

## ▶️ Running Locally

**Start API:**
```bash
uvicorn main:app --reload
```

**Start Streamlit Frontend:**
```bash
streamlit run app.py
```

---

## 📨 API Usage

**POST** `/recommend`

- **Request Body:**
```json
{
  "query": "Hiring for Python",
  "threshold": 0.4,
  "top_k": 10
}
```

- **Response:**
```json
{
  "results": [
    {
      "id": "50e6231d-8f64-4b66-aa39-1ad193826151",
      "name": "Python (New)",
      "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
      "remote_testing": true,
      "adaptive_irt": false,
      "duration": "11 minutes",
      "test_types": "Knowledge & Skills",
      "similarity": 0.536763163612078
    }
  ]
}
```

✅ You can also test the API at: [https://your-api-url/docs](https://your-api-url/docs)

---

## 📌 Notes

- The model used is `all-MiniLM-L6-v2` from HuggingFace for fast and accurate sentence embeddings.
- SHL product embeddings are stored in Supabase with vector indexing and similarity scoring.
- Threshold filtering is applied to ensure relevance of results.

---

## 🧑‍💻 Authors

- **Ayush Gupta** 

---
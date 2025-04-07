from fastapi import FastAPI, Request
from pydantic import BaseModel
from query import query_recommendations

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    threshold: float = 0.4
    top_k: int = 10

@app.get("/")
def read_root():
    return {"message": "✅ SHL RAG API is running."}

@app.post("/recommend")
def recommend(data: QueryRequest):
    results = query_recommendations(data.query, threshold=data.threshold, top_k=data.top_k)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

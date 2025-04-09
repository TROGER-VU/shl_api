from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from query import query_recommendations

app = FastAPI()

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Input model for /recommend
class RecommendRequest(BaseModel):
    query: str

# Output model for a single recommended assessment
class Assessment(BaseModel):
    url: str
    adaptive_support: str  # "Yes" or "No"
    description: str
    duration: int
    remote_support: str  # "Yes" or "No"
    test_type: List[str]

@app.get("/")
def read_root():
    return {"message": "✅ SHL RAG API is running."}

# Response model for /recommend
class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# Assessment Recommendation Endpoint
@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(data: RecommendRequest):
    try:
        results = query_recommendations(data.query, threshold=0.4, top_k=10)

        if not results:
            raise HTTPException(status_code=404, detail="No recommendations found.")

        formatted_results = []
        for item in results:
            formatted_results.append({
                "url": item.get("url", "#"),
                "adaptive_support": "Yes" if item.get("adaptive_irt") else "No",
                "description": item.get("name", "No description provided."),
                "duration": int(item.get("duration", "0").split()[0]) if "minute" in item.get("duration", "") else 0,
                "remote_support": "Yes" if item.get("remote_testing") else "No",
                "test_type": [t.strip() for t in item.get("test_types", "").split(",") if t.strip()]
            })

        return {"recommended_assessments": formatted_results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000)

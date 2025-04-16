from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from recommender import recommend_schemes

app = FastAPI()

# Allow CORS for frontend access (update origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    age: int
    gender: str
    caste: str
    income: float
    occupation: str

@app.post("/recommend")
def get_recommendations(user: UserInput):
    try:
        recommendations = recommend_schemes(user.dict())
        return {"eligible_schemes": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

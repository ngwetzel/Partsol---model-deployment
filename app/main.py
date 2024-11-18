from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import model_pipeline

app = FastAPI()

# Define the request body
class TextRequest(BaseModel):
    text: str

@app.post("/predict/")
def predict(request: TextRequest):
    try:
        # Perform sentiment analysis using the model pipeline
        result = model_pipeline(request.text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint to check if the service is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the sentiment analysis API"}

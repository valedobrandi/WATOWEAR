from fastapi import FastAPI, HTTPException, Request
from app.schemas import OutfitRequest, OutfitResponse
from app.services.ai_service import ai_service
from app.config import settings

app = FastAPI(
    title="WATOWEAR AI Stylist API",
    description="API to generate outfit recommendations based on wardrobe and context.",
    version="1.0.0"
)

# Custom Error Handler for a cleaner API
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc),
            "hint": "Check if the OpenAI API Key is valid and you have internet connection."
        },
    )

@app.get("/config-check")
def check_config():
    # Never return the actual API key in a real app! 
    # This is just to verify the key is loaded for your exercise.
    return {"model": settings.model_name, "key_loaded": bool(settings.openai_api_key)}

@app.get("/")
def read_root():
    return {"status": "online", "message": "Welcome to WATOWEAR API"}

@app.post("/generate-outfit", response_model=OutfitResponse)
async def generate_outfit(request: OutfitRequest):
    try:
        # Call the AI service
        result = await ai_service.generate_outfit_recommendation(request)
        return result
    except Exception as e:
        # The global handler we built earlier will also catch this, 
        # but handling it here allows for more specific AI-related logs.
        raise HTTPException(status_code=500, detail=f"AI Generation failed: {str(e)}")
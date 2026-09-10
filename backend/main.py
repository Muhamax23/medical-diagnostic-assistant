from fastapi import FastAPI

app = FastAPI(
    title="AI Medical Diagnostic Assistant",
    description="Clinical decision-support system for medical information and diagnostic assistance.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Medical Diagnostic Assistant API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
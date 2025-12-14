from fastapi import FastAPI
from app.webhook.tradingview import router as tradingview_router

app = FastAPI()

# IMPORTANT: prefix = /webhook
app.include_router(tradingview_router, prefix="/webhook")

@app.get("/")
def root():
    return {"message": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

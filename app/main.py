import os
from fastapi import FastAPI
from app.webhook.tradingview import router as tradingview_router

print("BOOTING APP...")
print("ENV TV_WEBHOOK_SECRET =", os.getenv("TV_WEBHOOK_SECRET"))

app = FastAPI()

app.include_router(tradingview_router, prefix="/webhook")

@app.get("/")
def root():
    return {"message": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}

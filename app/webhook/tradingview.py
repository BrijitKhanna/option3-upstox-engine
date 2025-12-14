from fastapi import APIRouter, Request, HTTPException
import os

router = APIRouter()

WEBHOOK_SECRET = os.getenv("TV_WEBHOOK_SECRET")
print("Loaded TV_WEBHOOK_SECRET:", WEBHOOK_SECRET)

@router.post("/tradingview")
async def tradingview_webhook(request: Request):
    payload = await request.json()

    if payload.get("secret") != WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Invalid secret")

    print("TradingView payload:", payload)

    return {"status": "received"}

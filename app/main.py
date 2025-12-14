from fastapi import FastAPI

app = FastAPI(title="Option 3 Upstox Engine")

@app.get("/health")
def health():
    return {"status": "ok"}
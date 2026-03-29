# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Req(BaseModel):
    symbol: str

@app.post("/signal")
def get_signal(req: Req):
    # Mocked logic: combine fake signals
    signal = random.choice(["BUY","HOLD","SELL"])
    confidence = round(random.uniform(0.6, 0.95),2)
    reason = "Volume spike + positive earnings comment (mocked)."
    return {"symbol": req.symbol, "signal": signal, "confidence": confidence, "reason": reason}

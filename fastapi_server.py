# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import asyncio

app = FastAPI(title="ANTARIKSH ASTRA SPATIAL INTELLIGENCE SERVER")

# Enable CORS for Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow the Vercel frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/api/query")
async def process_query(request: QueryRequest):
    query = request.query.lower()
    
    # Simulate Agentic Routing Delay
    await asyncio.sleep(2)
    
    if "deforestation" in query or "change" in query:
        return {
            "status": "success",
            "lat": 20.5937,
            "lng": 78.9629,
            "target_name": "DEFORESTATION FRONT, INDIA",
            "trace": "EXECUTING TRACE: VLM_ENCODER -> CHANGE_DETECTION -> MASKING...",
            "result": "RESULT: 2.4 SQ KM FOREST LOSS DETECTED. CONFIDENCE: 0.94. TRACE LOGGED."
        }
    elif "sar" in query or "cartosat" in query or "fusion" in query:
        return {
            "status": "success",
            "lat": 28.6139,
            "lng": 77.2090,
            "target_name": "RISAT-CARTOSAT ALIGNMENT, NEW DELHI",
            "trace": "EXECUTING TRACE: DOFA_SENSOR_ALIGNMENT -> SAR_OPTICAL_FUSION...",
            "result": "RESULT: UNAUTHORIZED CONSTRUCTION IDENTIFIED. CONFIDENCE: 0.88. TRACE LOGGED."
        }
    else:
        # Generic fallback using Gemini logic (stubbed for live demo safety)
        return {
            "status": "success",
            "lat": 22.9868,
            "lng": 87.8550,
            "target_name": "TARGET IDENTIFIED",
            "trace": "EXECUTING TRACE: GEMINI_VISION -> SPATIAL_QUERY...",
            "result": f"RESULT: ANALYSIS COMPLETE FOR '{request.query.upper()}'. NO ANOMALIES."
        }

if __name__ == '__main__':
    import uvicorn
    print("Starting ANTARIKSH ASTRA backend on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

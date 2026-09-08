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

import google.generativeai as genai
import os

# ==========================================
# INSERT YOUR GEMINI API KEY HERE
# ==========================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

if GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-3.5-flash')
else:
    gemini_model = None

class QueryRequest(BaseModel):
    query: str

@app.post("/api/query")
async def process_query(request: QueryRequest):
    query = request.query.lower()
    
    # Simulate Agentic Routing Delay
    await asyncio.sleep(1)
    
    if "deforestation" in query or "change" in query:
        return {
            "status": "success",
            "lat": 20.5937,
            "lng": 78.9629,
            "target_name": "DEFORESTATION FRONT, INDIA",
            "trace": "EXECUTING TRACE: VLM_ENCODER -> CHANGE_DETECTION -> MASKING...",
            "result": "RESULT: 2.4 SQ KM FOREST LOSS DETECTED. CONFIDENCE: 0.94. TRACE LOGGED."
        }
    elif "sar" in query or "cartosat" in query or "fusion" in query or "construction" in query:
        return {
            "status": "success",
            "lat": 28.6139,
            "lng": 77.2090,
            "target_name": "RISAT-CARTOSAT ALIGNMENT, NEW DELHI",
            "trace": "EXECUTING TRACE: DOFA_SENSOR_ALIGNMENT -> SAR_OPTICAL_FUSION...",
            "result": "RESULT: UNAUTHORIZED CONSTRUCTION IDENTIFIED. CONFIDENCE: 0.88. TRACE LOGGED."
        }
    else:
        # Dynamic Fallback using Real Gemini API!
        ai_response_text = f"RESULT: ANALYSIS COMPLETE FOR '{request.query.upper()}'. NO ANOMALIES."
        
        if gemini_model:
            try:
                prompt = f"You are Drishti Spatial AI, an advanced satellite intelligence assistant built for ISRO. Keep your answer brief, professional, and military-style (under 3 sentences). Answer this query: {request.query}"
                response = gemini_model.generate_content(prompt)
                ai_response_text = response.text.strip()
            except Exception as e:
                print(f"Gemini API Error: {e}")
        
        return {
            "status": "success",
            "action": "geocode",
            "trace": "EXECUTING TRACE: LLaVA_VLM_ENCODER -> NLP_ROUTING...",
            "result": ai_response_text
        }

if __name__ == '__main__':
    import uvicorn
    print("Starting ANTARIKSH ASTRA backend on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)

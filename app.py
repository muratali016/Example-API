from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# API endpoints
@app.post("/do_something")
async def generate_report(data: InputData):
    ...
    
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/migrate")
async def migrate_endpoint(files: List[UploadFile] = File(...), target_lang: str = Form("python")):
    # Hum pehli file ko process kar rahe hain
    content = await files[0].read()
    source = content.decode("utf-8", errors='ignore')
    return {"migrated_code": f"// Migrated to {target_lang}\n\n" + source, "original_code": source}

@app.post("/ai-suggest")
async def ai_suggest_endpoint(files: List[UploadFile] = File(...), language: str = Form("python")):
    content = await files[0].read()
    source = content.decode("utf-8", errors='ignore')
    return {"suggestions": "AI Suggestion logic here", "filename": files[0].filename}

@app.get("/")
def root():
    return {"message": "API is running"}

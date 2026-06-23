from fastapi import FastAPI, UploadFile, File
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
async def migrate_endpoint(files: List[UploadFile] = File(...)):
    content = await files[0].read()
    source = content.decode("utf-8", errors='ignore')
    return {"migrated_code": "// Migrated code result\n\n" + source, "original_code": source}

@app.post("/ai-suggest")
async def ai_suggest_endpoint(files: List[UploadFile] = File(...)):
    return {"suggestions": "AI Suggestion: Ye code kaafi purana hai, ise update karna chahiye!"}

@app.get("/")
def root():
    return {"message": "API is running"}

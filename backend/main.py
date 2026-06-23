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
    combined_code = ""
    for file in files:
        content = await file.read()
        source = content.decode("utf-8", errors='ignore')
        # Har file ka naam aur content add kar rahe hain
        combined_code += f"\n\n--- File: {file.filename} ---\n{source}"
    
    return {
        "migrated_code": f"// --- Migrated Content ---\n{combined_code}", 
        "original_code": combined_code
    }

@app.post("/ai-suggest")
async def ai_suggest_endpoint(files: List[UploadFile] = File(...)):
    # Yahan bhi sab files ke liye analysis kar sakte hain
    filenames = ", ".join([f.filename for f in files])
    suggestions = f"--- Analysis for: {filenames} ---\n\nMultiple files detected. Each file structure is being analyzed for migration."
    return {"suggestions": suggestions}

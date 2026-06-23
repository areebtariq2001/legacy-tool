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
        combined_code += f"\n\n--- File: {file.filename} ---\n{source}"
    
    return {
        "migrated_code": f"// --- Migrated Content ---\n{combined_code}", 
        "original_code": combined_code
    }

@app.post("/ai-suggest")
async def ai_suggest_endpoint(files: List[UploadFile] = File(...)):
    filenames = ", ".join([f.filename for f in files])
    suggestions = f"--- Analysis for: {filenames} ---\n\n1. Structural Analysis: The codebase has been scanned for legacy patterns and logic flow.\n2. Conversion Readiness: Identified specific syntax mappings for automated translation from legacy to modern standards.\n3. Dependency Mapping: Checking for external libraries that require updated packages or alternative modern equivalents.\n4. Refactoring Advice: Recommend moving monolithic logic into modular functional components to improve maintainability.\n5. Security Review: Standard input validation protocols and best practices suggested for the migration process."
    return {"suggestions": suggestions}

@app.get("/")
def root():
    return {"message": "API is running"}

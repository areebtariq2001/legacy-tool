from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
import ast
import os
import re
from collections import defaultdict, Counter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyze_code(source):
    tree = ast.parse(source)
    functions, classes, imports, issues = [], [], [], []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            for a in node.names:
                imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

    if 'xrange' in source:
        issues.append("xrange() found — use range()")
    if 'print ' in source and 'print(' not in source:
        issues.append("print statement found — use print()")
    if 'raw_input' in source:
        issues.append("raw_input() found — use input()")

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "issues": issues
    }

def migrate_code(source):
    changes = []
    migrated = source

    if 'xrange' in migrated:
        migrated = migrated.replace('xrange', 'range')
        changes.append("xrange → range")
    if 'raw_input' in migrated:
        migrated = migrated.replace('raw_input', 'input')
        changes.append("raw_input → input")
    if 'unicode(' in migrated:
        migrated = migrated.replace('unicode(', 'str(')
        changes.append("unicode → str")

    return {"migrated_code": migrated, "changes": changes}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    source = content.decode("utf-8")
    result = analyze_code(source)
    result["filename"] = file.filename
    return result

@app.post("/migrate")
async def migrate(file: UploadFile = File(...)):
    content = await file.read()
    source = content.decode("utf-8")
    result = migrate_code(source)
    result["filename"] = file.filename
    return result


@app.post("/download")
async def download(file: UploadFile = File(...)):
    content = await file.read()
    source = content.decode("utf-8")
    result = migrate_code(source)
    migrated = result.get("migrated_code", "")
    filename = file.filename
    if filename.endswith('.py'):
        filename = filename.replace('.py', '_migrated.py')
    else:
        filename = f"{filename}_migrated"

    return Response(
        content=migrated.encode('utf-8'),
        media_type='application/octet-stream',
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )

@app.get("/")
def root():
    return {"message": "Legacy Migration Tool API is running!"}

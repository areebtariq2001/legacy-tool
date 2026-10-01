main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: add a module-level secret key for certificate signing, near other secret-reading code
old1 = 'def _check_admin_auth(request: Request):'
new1 = '''_CERT_SIGNING_KEY = os.environ.get("CERTIFICATE_SIGNING_KEY", "") or secrets.token_hex(32)


def _check_admin_auth(request: Request):'''
results["1_add_secret_key"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: change issue() to sign with HMAC instead of plain SHA-256
old2 = '            cert_data = json.dumps(certificate, sort_keys=True)\n            certificate["certificate_signature"] = hashlib.sha256(cert_data.encode()).hexdigest()'
new2 = '            cert_data = json.dumps(certificate, sort_keys=True)\n            certificate["certificate_signature"] = hmac.new(_CERT_SIGNING_KEY.encode(), cert_data.encode(), hashlib.sha256).hexdigest()'
results["2_issue_use_hmac"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: change verify() to recompute with HMAC instead of plain SHA-256
old3 = '        expected = hashlib.sha256(json.dumps(cert, sort_keys=True).encode()).hexdigest()'
new3 = '        expected = hmac.new(_CERT_SIGNING_KEY.encode(), json.dumps(cert, sort_keys=True).encode(), hashlib.sha256).hexdigest()'
results["3_verify_use_hmac"] = content.count(old3)
content = content.replace(old3, new3, 1)

# Fix 4: add auth check + use real authenticated email in the endpoint
old4 = '''async def issue_migration_certificate_endpoint(request: Request):
    try:
        _body = await request.json()
        _filename = str(_body.get("filename", "unknown"))[:500]
        _reviewer_notes = str(_body.get("reviewer_notes", ""))[:5000]
        _decision = str(_body.get("decision", "Approved"))[:50]
        _original_hash = hashlib.sha256(_filename.encode()).hexdigest()[:16]
        _migrated_hash = hashlib.sha256(_reviewer_notes.encode()).hexdigest()[:16]
        _approved = _decision.strip().lower() == "approved"
        cert = cert_manager.issue(
            filename=_filename, original_hash=_original_hash, migrated_hash=_migrated_hash,
            confidence=100 if _approved else 0, reviewer_email="reviewer", approved=_approved
        )'''
new4 = '''async def issue_migration_certificate_endpoint(request: Request):
    try:
        _reviewer_email = _check_user_auth(request)
        if not _reviewer_email:
            return JSONResponse(status_code=401, content={"error": "Unauthorized - please log in to issue a migration certificate"})
        _body = await request.json()
        _filename = str(_body.get("filename", "unknown"))[:500]
        _reviewer_notes = str(_body.get("reviewer_notes", ""))[:5000]
        _decision = str(_body.get("decision", "Approved"))[:50]
        _original_hash = hashlib.sha256(_filename.encode()).hexdigest()[:16]
        _migrated_hash = hashlib.sha256(_reviewer_notes.encode()).hexdigest()[:16]
        _approved = _decision.strip().lower() == "approved"
        cert = cert_manager.issue(
            filename=_filename, original_hash=_original_hash, migrated_hash=_migrated_hash,
            confidence=100 if _approved else 0, reviewer_email=_reviewer_email, approved=_approved
        )'''
results["4_add_auth_real_email"] = content.count(old4)
content = content.replace(old4, new4, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXCERT-DONE")
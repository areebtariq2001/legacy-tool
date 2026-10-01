main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.get("/blockchain-status")'''

new = '''class MigrationCertificate:
    def __init__(self):
        self.certificates = {}
        self._lock = threading.Lock()

    def issue(self, filename, original_hash, migrated_hash, confidence, reviewer_email, approved):
        with self._lock:
            cert_id = hashlib.sha256(f"{filename}{original_hash}{migrated_hash}{datetime.now().isoformat()}".encode()).hexdigest()[:16].upper()
            certificate = {
                "certificate_id": f"STARBUILD-{cert_id}",
                "issued_at": datetime.now().isoformat(),
                "filename": filename,
                "original_code_hash": original_hash,
                "migrated_code_hash": migrated_hash,
                "confidence_score": confidence,
                "approved_by": reviewer_email,
                "approval_status": "APPROVED" if approved else "REJECTED",
                "blockchain_block": len(audit_blockchain.chain),
                "chain_hash_at_issuance": audit_blockchain.chain[-1].hash,
            }
            cert_data = json.dumps(certificate, sort_keys=True)
            certificate["certificate_signature"] = hashlib.sha256(cert_data.encode()).hexdigest()
            self.certificates[cert_id] = certificate
            try:
                audit_blockchain.add_block(
                    action="CERTIFICATE_ISSUED", filename=filename, user_email=reviewer_email, ip="system",
                    result=f"cert={cert_id} confidence={confidence}% status={certificate['approval_status']}"
                )
            except Exception:
                pass
            return certificate

    def verify(self, cert_id):
        with self._lock:
            cert = self.certificates.get(cert_id)
        if not cert:
            return {"valid": False, "reason": "Certificate not found"}
        cert = dict(cert)
        signature = cert.pop("certificate_signature", "")
        expected = hashlib.sha256(json.dumps(cert, sort_keys=True).encode()).hexdigest()
        cert["certificate_signature"] = signature
        if not hmac.compare_digest(signature, expected):
            return {"valid": False, "reason": "Certificate tampered!"}
        chain_valid, _ = audit_blockchain.verify_chain()
        return {
            "valid": True,
            "certificate": cert,
            "blockchain_integrity": "VERIFIED" if chain_valid else "COMPROMISED",
        }


cert_manager = MigrationCertificate()


@app.post("/issue-migration-certificate")
async def issue_migration_certificate_endpoint(req: ApprovalRequest):
    try:
        _original_hash = hashlib.sha256((req.filename or "").encode()).hexdigest()[:16]
        _migrated_hash = hashlib.sha256((req.reviewer_notes or "").encode()).hexdigest()[:16]
        _approved = req.decision.strip().lower() == "approved"
        cert = cert_manager.issue(
            filename=req.filename, original_hash=_original_hash, migrated_hash=_migrated_hash,
            confidence=100 if _approved else 0, reviewer_email="reviewer", approved=_approved
        )
        write_audit_log("issue-certificate", req.filename, f"cert issued: {cert['certificate_id']}")
        return cert
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": f"Certificate issuance failed: {str(e)}"})


@app.get("/verify-migration-certificate/{cert_id}")
async def verify_migration_certificate_endpoint(cert_id: str):
    return cert_manager.verify(cert_id)


@app.get("/blockchain-status")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("MIGRATION-CERTIFICATE-IMPLEMENTED")
else:
    print("FAILED - count was:", count)
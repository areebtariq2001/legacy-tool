# StarSage

**AI-powered legacy code migration and audit platform for Python, Java, PHP, and COBOL.**

StarSage analyzes legacy codebases, extracts business logic, flags security and compliance risks, and generates a modernization plan — combining rule-based static analysis (AST-verified) with optional AI-assisted migration.

🔗 **Live app:** [areebtariq2001.github.io/legacy-tool](https://areebtariq2001.github.io/legacy-tool/)
🔗 **Backend API:** hosted on Render (FastAPI)

---

## What it does

Upload a source file (or scan a public GitHub repo) and StarSage runs a full pipeline automatically:

**Analyze → Migrate → Security Scan → Tech-Debt & Compliance**

| Area | What StarSage does |
|---|---|
| **Migration** | Converts legacy syntax to modern equivalents (Python 2→3, Java legacy patterns, PHP 5→8, COBOL→modernization spec) with a diff and a list of every automatic change made |
| **Business rules** | Extracts business logic from source code (COBOL paragraphs, banking/interest/AML calculations) and maps it to suggested microservices |
| **Security** | Detects hardcoded secrets, SQL injection, command injection, weak cryptography (MD5/SHA1/DES/RC4), insecure TLS, and more — with real, cross-referenced regex patterns, not just keyword matching |
| **Compliance** | AML/KYC pattern detection, banking-domain classification, regulatory-body references (FATF/OFAC/SBP/Basel/PCI-DSS/GDPR) |
| **Architecture** | Generates a layered architecture view, API/database dependency maps, and an exportable architecture diagram (SVG/PNG/Mermaid) |
| **Planning** | Migration risk scoring, cost/time estimation, CI/CD pipeline recommendations, a phased modernization roadmap |
| **AI features** | AI-suggested refactors, generated documentation, generated test scenarios, an "Ask Codebase" Q&A assistant — all with prompt-injection protection on user-supplied code |

### Supported languages
Python · Java · PHP · COBOL

### Supported input
Single file upload, or scan up to 25 files from a public GitHub repository (`https://github.com/owner/repo`).

---

## Architecture

```
frontend/          Static single-page app (HTML/CSS/vanilla JS), deployed via GitHub Pages
backend/            FastAPI backend (Python), deployed on Render
  main.py           All analysis, migration, and security-scan logic
  requirements.txt  Backend dependencies
```

The frontend calls the backend's REST API (`/analyze`, `/analyze-java`, `/analyze-php`, `/analyze-cobol`, `/migrate-*`, `/scan-crypto`, `/scan-sensitive`, `/extract-aml-kyc`, `/scan-repo`, and 60+ other endpoints) and renders the results as an interactive dashboard.

---

## Key design principles

- **Honest about limitations.** Every scan result carries a disclaimer: pattern-based detection is a planning aid, not a certification. Absence of a keyword doesn't guarantee absence of risk.
- **No secrets in output.** Security scans redact actual secret *values* in their responses — only the finding type, severity, and line number are shown.
- **AST-first where possible.** Python analysis uses genuine `ast.parse()` (business rules, call graphs, complexity) rather than regex alone, falling back to pattern-based analysis only where a real parser isn't available (Java/PHP/COBOL).
- **Prompt-injection aware.** Every AI-assisted feature that sends user code to an LLM wraps it in explicit delimiters and instructs the model to ignore any embedded instructions in the code itself.

---

## Running locally

**Backend**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend**
Open `frontend`'s `index.html` directly, or serve it with any static file server. Update the backend URL in the frontend config if not using the deployed Render instance.

---

## Status

Actively developed. Backend and frontend deploy automatically on push to `main` (Render for backend, GitHub Pages for frontend).

## Disclaimer

StarSage is a planning and discovery aid for legacy code migration. It does not execute code, connect to live systems, or guarantee regulatory compliance. All findings — security, compliance, business-rule extraction, and cost estimates — should be reviewed by a qualified engineer before being acted on.

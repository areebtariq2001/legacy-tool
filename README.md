StarBuild

AI-Powered Legacy Code Migration & Security Audit Platform

StarBuild helps banks, fintechs, and enterprises understand, audit, and safely modernize their legacy code (COBOL, older Java, Python 2, PHP). Instead of blindly converting old code, StarBuild understands it first — mapping its data, dependencies, security risks, and business logic — so migration is safe, predictable, and audit-ready.


Philosophy: Understand first, migrate second.




🔗 Live Links

ResourceURLLive Toolhttps://areebtariq2001.github.io/legacy-tool/API (Backend)https://legacy-migration-tool-1.onrender.comAPI Docs (Swagger)https://legacy-migration-tool-1.onrender.com/docs


Note: The backend runs on a free tier that sleeps when idle. Open the API URL once to wake it (~50s) before a live demo.




Why StarBuild

Legacy systems run critical banking operations, but they are hard to understand, poorly documented, and risky to change. StarBuild reduces that risk by giving teams a clear, verified picture of the code before they touch it — with honest confidence scores on every automated change.

Four core benefits:


💰 Saves money — work that consultants do in weeks, done in minutes
⏰ Saves time — understand legacy code at a glance
🛡️ Reduces risk — audit before you migrate, with rollback planning
✅ Security & compliance — catch issues aligned to PCI-DSS, GDPR, SBP, Basel III, AML/KYC



Features (44+)

Core Analysis & Migration

Analyze · Migrate (rule-based) · AI Migrate (guardrails + confidence score) · Call Graph · Risk Check · Tech Debt · Gen Docs

Security & Compliance

Data Scan · Crypto Scan · Quantum-Readiness Score (unique) · Banking Scan · AML/KYC Extractor · Compliance Mapping · SQL Injection Scanner · PII Detection · Key Management Audit · Zero-Trust Readiness Score (unique)

Enterprise Analysis

Repository Scan · Database Schema Analysis · API Dependency Mapping · Architecture View · CI/CD Recommendations · AI-Native Readiness (unique) · Migration Risk Prediction · Cost Estimator · Tech Stack Detector · Vendor Lock-in Risk Analysis

Banking-Specific

Business Rule Extractor (AI) · Business Rules Engine (compliance tagging) · Executive Report · Audit-Ready PDF Export · Impact Analysis · Transaction Flow Mapping · Rollback Plan · Regional Compliance Mapping (SBP/Global) · Regulatory Framework Presets (SBP, Basel III, PCI-DSS, GDPR)

Developer Workflow

Codebase Q&A — ask plain-English questions about an uploaded legacy file and get an AI-grounded answer · GitHub Webhook Receiver — auto-scan changed Python files on push · Sandbox Test — lightweight, resource-limited execution check for migrated code


On-Premise AI (Ollama)

Banks won't send proprietary code to a third-party cloud API. StarBuild supports on-premise AI via Ollama:


Switchable AI provider (AI_PROVIDER=ollama or groq) with automatic fallback
Runs entirely on the bank's own infrastructure — no code leaves the premises
Same guardrails and confidence scoring apply regardless of provider
Built-in error detection: if the AI provider fails, the system transparently falls back to deterministic rule-based migration rather than silently returning a bad result



How It Works


Choose a language (Python, Java, PHP, COBOL) and a mode
Upload one or more code files, or paste a public GitHub repo URL
StarBuild analyzes and returns results instantly — scores, findings, maps, or reports
Download reports (PDF / CSV / JSON) to share with your team, managers, or auditors



Tech Stack


Frontend: React (deployed on GitHub Pages)
Backend: FastAPI (Python), deployed on Render
AI: Groq (cloud) or Ollama (on-premise), with automatic provider switching
Analysis: Python AST + pattern-based static analysis



Honest Status & Roadmap

StarBuild today is a working prototype with 44+ features, built by a solo developer. It is a strong assessment and audit tool, not yet a certified banking-grade platform.

Known limitations (stated honestly):


The Sandbox Test feature is a lightweight, resource-limited subprocess check — not a fully isolated Docker sandbox. It should only be used with trusted, already-migrated code.
The GitHub Webhook Receiver scans changed files on push; full CI/CD integration (auto-generating a migration pull request) requires GitHub App write-access setup, which is planned.
The Human-in-the-Loop Approval log and Migration Registry Dashboard use file-based demo storage — data resets if the server restarts. For a real audit trail (which regulators require to be permanent and tamper-proof), this needs a persistent database (e.g. PostgreSQL), which is a concrete infrastructure requirement on the roadmap.


Roadmap:


SOC 2 certification & independent security audit
On-premise / private cloud deployment with RBAC and full audit trails
Fully isolated Docker-based (or external service-based) sandbox execution
GitHub App integration for automated pull request generation


We believe honesty is a strength: banks value accuracy, explainability, and auditability — and StarBuild already delivers early versions of all three. Every scan includes a disclaimer, and no result is presented as a certified guarantee.


Disclaimer

StarBuild's analyses are automated aids for planning and review. They are pattern-based and may include false positives. Always confirm findings with a qualified security review, compliance officer, and domain experts before making migration decisions.


StarBuild — Predictable, AST-verified, audit-ready legacy migration.

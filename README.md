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



Features (48+)

Core Analysis & Migration

Analyze · Migrate (rule-based) · AI Migrate (guardrails + confidence score) · Call Graph · Risk Check · Tech Debt · Gen Docs

Security & Compliance

Data Scan · Crypto Scan · Quantum-Readiness Score (unique) · Banking Scan · AML/KYC Extractor · Compliance Mapping · SQL Injection Scanner · PII Detection · Key Management Audit · Zero-Trust Readiness Score (unique)

Enterprise Analysis

Repository Scan (GitHub-authenticated, 5000 requests/hour) · Database Schema Analysis · API Dependency Mapping · Architecture View · CI/CD Recommendations · AI-Native Readiness (unique) · Migration Risk Prediction · Cost Estimator · Tech Stack Detector · Vendor Lock-in Risk Analysis

Banking-Specific

Business Rule Extractor (AI) · Business Rules Engine (compliance tagging) · Executive Report · Audit-Ready PDF Export · Impact Analysis · Transaction Flow Mapping · Rollback Plan · Regional Compliance Mapping (SBP/Global) · Regulatory Framework Presets (SBP, Basel III, PCI-DSS, GDPR)

Developer Workflow

Codebase Q&A · GitHub Webhook Receiver (auto-scan on push) · Sandbox Test (lightweight execution check)

Governance & Traceability

Human-in-the-Loop Approval — reviewer decisions (Approve/Reject/Modify) logged with notes · Code Quality Score — complexity, readability, and comment-density grading · Migration Registry Dashboard — aggregated approval stats and recent activity · Migration Roadmap Generator — repo-wide, risk-prioritized migration phases (Low → Medium → High risk)


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
GitHub Integration: Authenticated API access (5000 req/hour) for repository scanning



Verified, Not Just Claimed

Every feature listed here has been manually tested against real inputs, with raw API responses checked line-by-line — not just UI screenshots. This process has already caught and fixed real bugs before they reached users:


A confidence-scoring bug where AI service errors were silently marked "high confidence" instead of triggering a safe fallback
A code-quality grading bug where "High complexity" code could still receive a Grade A
A migration-roadmap bug where files were bucketed into the wrong risk phase due to a string-matching error
A GitHub API rate-limiting issue that would have affected any user scanning multiple repositories


We treat "it returns 200 OK" and "the business logic is actually correct" as two different bars — and verify against the second one.


Honest Status & Roadmap

StarBuild today is a working prototype with 48+ features, built by a solo developer with an advisor and marketing collaborator. It is a strong assessment, audit, and governance tool, not yet a certified banking-grade platform.

Known limitations (stated honestly):


The Sandbox Test feature is a lightweight, resource-limited subprocess check — not a fully isolated Docker sandbox. Use only with trusted, already-migrated code.
Approval-log and dashboard data is currently stored in-memory/file-based and resets on server restart. Persistent database storage (PostgreSQL) is required before this can serve as a real audit trail — this is a concrete, fundable infrastructure gap.
The GitHub Webhook Receiver scans changed files on push; full CI/CD integration (auto-generating a migration pull request) requires GitHub App write-access setup.


Roadmap:


Persistent database for audit-trail data (PostgreSQL)
SOC 2 certification & independent security audit
On-premise / private cloud deployment with RBAC and full audit trails
Fully isolated Docker-based sandbox execution
GitHub App integration for automated pull request generation


We believe honesty is a strength: banks value accuracy, explainability, and auditability — and StarBuild already delivers early, verified versions of all three. Every scan includes a disclaimer, and no result is presented as a certified guarantee.


Disclaimer

StarBuild's analyses are automated aids for planning and review. They are pattern-based and may include false positives. Always confirm findings with a qualified security review, compliance officer, and domain experts before making migration decisions.


StarBuild — Predictable, AST-verified, audit-ready legacy migration

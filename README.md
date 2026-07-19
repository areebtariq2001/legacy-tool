# StarBuild

### AI-Powered Legacy Code Migration & Security Audit Platform

StarBuild helps banks, fintechs, and enterprises **understand, audit, and safely modernize** their legacy code (Python, Java, PHP, COBOL). Instead of blindly converting old code, StarBuild understands it first — mapping its data, dependencies, security risks, and business logic — so migration is safe, predictable, and audit-ready.

> **Philosophy:** Understand first, migrate second.

---

## 🔗 Live Links

| Resource | URL |
|----------|-----|
| **Live Tool** | https://areebtariq2001.github.io/legacy-tool/ |
| **API (Backend)** | https://legacy-migration-tool-1.onrender.com |
| **API Docs (Swagger)** | https://legacy-migration-tool-1.onrender.com/docs |

> **Note:** The backend runs on a free tier that sleeps when idle. Open the API URL once to wake it (~50s) before a live demo.

---

## Why StarBuild

Legacy systems run critical banking operations, but they are hard to understand, poorly documented, and risky to change. StarBuild reduces that risk by giving teams a clear, verified picture of the code **before** they touch it — with honest confidence scores on every automated change, and honest "not analyzed" messages instead of misleading silence when a check genuinely can't run.

**Four core benefits:**
- 💰 **Saves money** — work that consultants do in weeks, done in minutes
- ⏰ **Saves time** — understand legacy code at a glance
- 🛡️ **Reduces risk** — audit before you migrate, with rollback planning
- ✅ **Security & compliance** — catch issues aligned to PCI-DSS, GDPR, SBP, Basel III, AML/KYC

---

## Features (59+)

### Core Analysis & Migration
Analyze · Migrate (rule-based) · AI Migrate (guardrails + confidence score) · Call Graph · Risk Check · Tech Debt · Gen Docs

### Security & Compliance
Data Scan · Crypto Scan · **Quantum-Readiness Score** *(unique)* · Banking Scan · AML/KYC Extractor · SQL Injection Scanner · PII Detection · Key Management Audit · **Zero-Trust Readiness Score** *(unique)*

### Enterprise Analysis
Repository Scan (GitHub-authenticated) · Database Schema Analysis · API Dependency Mapping · Architecture View · CI/CD Recommendations · **AI-Native Readiness** *(unique)* · Migration Risk Prediction · Cost Estimator · Tech Stack Detector · Vendor Lock-in Risk Analysis

### Banking-Specific
Business Rule Extractor (AI) · Business Rules Engine (compliance tagging) · Executive Report · Audit-Ready PDF Export · Impact Analysis · Transaction Flow Mapping · Rollback Plan · Regional Compliance Mapping · Regulatory Framework Presets (SBP, Basel III, PCI-DSS, GDPR)

### Developer Workflow
Codebase Q&A · GitHub Webhook Receiver · Sandbox Test (lightweight execution check)

### Governance & Traceability
Human-in-the-Loop Approval (persistent, database-backed) · Code Quality Score · Migration Registry Dashboard · Migration Roadmap Generator

### Refactoring Depth (Phase 1)
Before/After Complexity Score · Code Smell Detector (long functions, deep nesting, duplicate code) · Refactoring Suggestions

### Replatforming Depth (Phase 2)
Platform Compatibility Checker (OS-specific code, shell calls) · Dependency Portability Score · Config Migration Helper (with credential detection)

### Re-architecting Formalization (Phase 3)
Re-architecture Readiness Report · Natural Service Boundary Detector

### Decision Support (Phase 4)
Migration Strategy Recommendation Engine (Rehost vs Refactor vs Rebuild) · ROI Calculator

---

## Multi-Language Support

StarBuild supports **Python, Java, PHP, and COBOL**. Python has the deepest feature coverage; Java has been extensively tested and hardened — including method detection (handling `throws`/`synchronized`), wildcard import parsing, comment-aware analysis, and language-agnostic security patterns (SQL injection, hardcoded credentials work the same way regardless of language).

Where a check is genuinely Python-only (e.g. AST-based parsing), StarBuild **honestly reports "Not Analyzed"** rather than silently returning a misleading "no risk found" result.

---

## On-Premise AI (Ollama)

Banks won't send proprietary code to a third-party cloud API. StarBuild supports **on-premise AI** via Ollama:

- Switchable AI provider (`AI_PROVIDER=ollama` or `groq`) with automatic fallback
- Runs entirely on the bank's own infrastructure — no code leaves the premises
- Built-in error detection: if the AI provider fails, the system transparently falls back to deterministic rule-based migration rather than silently returning a bad result

---

## Persistent, Auditable Data

Human-in-the-loop approval decisions are stored in a **persistent PostgreSQL database** (not a temporary file), so audit history survives server restarts — a requirement for any real compliance use case. A local-file fallback exists for resilience if the database is temporarily unreachable.

---

## How It Works

1. Choose a language (Python, Java, PHP, COBOL) and a mode
2. Upload one or more code files, or paste a public GitHub repo URL
3. StarBuild analyzes and returns results instantly — scores, findings, maps, or reports
4. Download reports (PDF / CSV / JSON) to share with your team, managers, or auditors

---

## Tech Stack

- **Frontend:** React (deployed on GitHub Pages)
- **Backend:** FastAPI (Python), deployed on Render
- **Database:** PostgreSQL (Supabase) for persistent audit logs
- **AI:** Groq (cloud) or Ollama (on-premise), with automatic provider switching
- **Analysis:** Python AST + language-aware pattern-based static analysis

---

## Verified, Not Just Claimed

Every feature in this repository has been manually tested against real code — Python and Java — with raw API responses checked line-by-line, not just UI screenshots. This process has caught and fixed over 30 real bugs before they reached users, including:

- Silent "no risk found" results on unsupported languages, now replaced with honest "Not Analyzed" messages
- A breaking Java migration bug (`Vector→ArrayList` conversion without converting the associated method calls)
- Cross-feature inconsistencies (e.g. a security-flagged file scoring "0% risk")
- False positives from comment text being parsed as code

We treat "it returns 200 OK" and "the business logic is actually correct" as two different bars — and verify against the second one.

---

## Honest Status & Roadmap

StarBuild today is a **working prototype with 59+ features**, built by a solo developer with a technical advisor and marketing collaborator. It is a strong **assessment, audit, and governance** tool, not yet a certified banking-grade platform.

**Known limitations (stated honestly):**
- The Sandbox Test feature is a lightweight, resource-limited subprocess check — not a fully isolated Docker sandbox.
- The GitHub Webhook Receiver scans changed files on push; full CI/CD integration (auto-generating a migration pull request) requires GitHub App write-access setup.
- PHP and COBOL support exists but has not yet received the same depth of testing as Python and Java.

**Roadmap:**
- SOC 2 certification & independent security audit
- Fully isolated Docker-based sandbox execution
- GitHub App integration for automated pull request generation
- Extend the same multi-language rigor (method detection, comment-awareness) to PHP and COBOL
- Characterization testing (before/after behavioral comparison)
- Codebase history intelligence via GitHub API (commit/author/change-frequency analysis)

---

## Disclaimer

StarBuild's analyses are automated aids for planning and review. They are pattern-based and may include false positives. Always confirm findings with a qualified security review, compliance officer, and domain experts before making migration decisions.

---

*StarBuild — Predictable, AST-verified, audit-ready legacy migration.*

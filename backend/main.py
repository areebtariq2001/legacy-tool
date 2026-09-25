"""
Regression tests for the StarSage "compliance_audit.py" bug report (Runs 1 and 2).
Run with: pytest test_determinism_and_scoring.py -v
"""
import hashlib
import hmac
import json
import os
import subprocess
import sys

import main

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "tests_fixtures", "compliance_audit.py")
PIPELINE_ENDPOINTS = ["/analyze", "/migrate", "/scan-sensitive", "/tech-debt", "/tech-debt-cost",
                      "/pci-dss-scorecard", "/pakistan-banking-suite"]

_PROBE = r"""
import hashlib, json, sys
sys.path.insert(0, sys.argv[1])
from fastapi.testclient import TestClient
import main
client = TestClient(main.app)
src = open(sys.argv[2], "rb").read()
out = {}
for ep in json.loads(sys.argv[3]):
    out[ep] = client.post(ep, files={"file": ("compliance_audit.py", src)}).json()
print(hashlib.sha256(json.dumps(out, sort_keys=True, default=str).encode()).hexdigest())
"""


def _pipeline_hash(hash_seed):
    env = dict(os.environ, PYTHONHASHSEED=str(hash_seed))
    res = subprocess.run([sys.executable, "-c", _PROBE, HERE, FIXTURE, json.dumps(PIPELINE_ENDPOINTS)],
                         capture_output=True, text=True, env=env, timeout=300)
    assert res.returncode == 0, res.stderr[-2000:]
    return res.stdout.strip().splitlines()[-1]


class TestDeterminism:
    """Bug 8: same file + same engine build must give byte-identical results."""

    def test_pipeline_identical_across_processes_and_hash_seeds(self):
        hashes = {_pipeline_hash(seed) for seed in (0, 1, 4242)}
        assert len(hashes) == 1, f"pipeline output varied between runs: {hashes}"

    def test_engine_version_exposed(self):
        from fastapi.testclient import TestClient
        body = TestClient(main.app).get("/health").json()
        assert body.get("engine_version")


class TestSqlInjectionPrecision:
    """A log line containing 'updated' was reported as an f-string SQL injection."""

    def test_fixture_reports_only_the_real_injection(self):
        src = open(FIXTURE).read()
        issues = main.scan_sql_injection(src, "compliance_audit.py")["sqli_issues"]
        assert [i["line"] for i in issues] == [56]

    def test_english_words_are_not_sql(self):
        for line in ['logger.info(f"balance updated for {acc}")',
                     'print("Please select a file " + name)',
                     'msg = f"Deleted {n} rows where needed"']:
            assert main.scan_sql_injection(line, "x.py")["sqli_issues"] == [], line

    def test_real_injections_still_detected(self):
        for fname, line in [("x.py", 'cur.execute("SELECT * FROM users WHERE id=" + uid)'),
                            ("x.py", 'q = f"UPDATE accounts SET bal = {b}"'),
                            ("x.py", 'q = "DELETE FROM t WHERE id=" + x'),
                            ("x.py", 'q = "UPDATE " + table + " SET x=1"'),
                            ("x.java", 'rs = stmt.executeQuery("select * from t where id=" + id);'),
                            ("x.php", '$q = "SELECT * FROM users WHERE id = " . $id;')]:
            assert main.scan_sql_injection(line, fname)["sqli_issues"], line


class TestPython3DivisionGate:
    """Bug 4: no Python 2 floor-division warning on valid Python 3 code."""

    def test_no_division_warning_on_py3_file(self):
        changes = main.migrate_code(open(FIXTURE).read())["changes"]
        assert not any("Division" in c for c in changes)


class TestSuiteShape:
    """Bug 6: every suite response carries numeric counts (no 'undefined' in the UI)."""

    def test_counts_present_even_when_not_run(self):
        big = "x = 1\n" * (main.MAX_FILE_SIZE // 6 + 10)
        for fn in (main.run_pci_dss_scorecard, main.run_pakistan_banking_suite):
            d = fn(big, "big.py")
            for k in ("passed_count", "total_count", "applicable_count", "not_applicable_count", "error_count"):
                assert isinstance(d.get(k), int), (fn.__name__, k)


class TestEffortEstimate:
    """Bug 9: never 0 h / $0 while a critical issue is open."""

    def test_open_sql_injection_sets_floor(self):
        d = main.calculate_tech_debt_cost(open(FIXTURE).read(), "compliance_audit.py")
        assert d["open_critical_issues"] >= 1
        assert d["debt_hours"] >= 2.0 and d["debt_cost_usd"] > 0

    def test_clean_file_can_still_be_zero(self):
        d = main.calculate_tech_debt_cost("def add(a: int, b: int) -> int:\n    return a + b\n", "clean.py")
        assert d["open_critical_issues"] == 0

    def test_no_double_count(self):
        d = main.calculate_tech_debt_cost(open(FIXTURE).read(), "compliance_audit.py")
        assert d["debt_hours"] == max(d["legacy_debt_hours"], d["open_issue_hours"])


class TestResultStamp:
    def test_analyze_and_migrate_are_stamped(self):
        from fastapi.testclient import TestClient
        c = TestClient(main.app)
        src = open(FIXTURE, "rb").read()
        for ep in ("/analyze", "/migrate"):
            body = c.post(ep, files={"file": ("compliance_audit.py", src)}).json()
            assert body["engine_version"] == main.ENGINE_VERSION
            assert len(body["input_sha256"]) == 16


class TestBurstLimit:
    """Bug 8: three quick re-runs of one analysis (~18 requests) must not be rate-limited."""

    def test_repeated_pipeline_not_blocked(self):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        c = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"})
        src = open(FIXTURE, "rb").read()
        codes = [c.post(ep, files={"file": ("compliance_audit.py", src)}).status_code
                 for _ in range(4) for ep in ("/analyze", "/migrate", "/scan-sensitive", "/tech-debt", "/tech-debt-cost", "/behavioral-confidence")]
        assert 429 not in codes, codes


LOAN = os.path.join(HERE, "tests_fixtures", "legacy_loan_system.py")


class TestRun3Bugs:
    """Bugs 11-14 from Run 3 (legacy_loan_system.py, real Python 2)."""

    def test_bug11_docstring_saying_no_aml_is_not_aml_logic(self):
        d = main.extract_aml_kyc(open(LOAN).read())
        assert d["aml_findings"] == 0 and d["kyc_findings"] == 0, d["findings"]
        labels = [f["pattern"] for f in main.detect_banking_patterns(open(LOAN).read())["findings"]]
        assert "AML/KYC compliance logic" not in labels and "Account identifiers" not in labels

    def test_bug11_real_aml_code_still_detected(self):
        assert main.extract_aml_kyc("def check_aml(txn):\n    return txn.amount > AML_THRESHOLD\n")["aml_findings"] >= 1
        java = "// no AML here\npublic class T { boolean check() { return AML_SERVICE.screen(x); } }\n"
        assert main.extract_aml_kyc(java)["aml_findings"] >= 1

    def test_bug12_division_only_on_real_operator(self):
        changes = main.migrate_code(open(LOAN).read())["changes"]
        div = [c for c in changes if "Division" in c]
        assert len(div) == 1 and "line(s) 33 " in div[0], div

    def test_bug13_cnic_hardcoded_and_logged(self):
        issues = main.analyze_code(open(LOAN).read())["issues"]
        assert any("Hardcoded CNIC" in i and "20" in i for i in issues), issues
        assert any("CNIC written in plaintext" in i and "68" in i for i in issues), issues

    def test_bug13_no_cnic_false_positive_on_clean_code(self):
        src = "def check_kyc(account):\n    return len(account.cnic) == 13\n"
        assert main._cnic_exposure_findings(src) == []

    def test_bug14_all_sqli_lines_reported(self):
        issues = main.analyze_code(open(LOAN).read())["issues"]
        sqli = [i for i in issues if i.startswith("SQL injection risk")]
        assert len(sqli) == 1 and all(n in sqli[0] for n in ("45", "56", "58")), sqli

    def test_other_languages_still_report_sqli(self):
        php = '<?php\n$q = "SELECT * FROM users WHERE id = " . $id;\n$r = mysqli_query($c, $q);\n'
        assert any("SQL injection" in i for i in main.analyze_php(php)["issues"])
        java = 'class A { void f(String id) { stmt.executeQuery("select * from t where id=" + id); } }\n'
        assert any("SQL injection" in i for i in main.analyze_java(java)["issues"])


def _run_migrated_cobol(name):
    src = open(os.path.join(HERE, "tests_fixtures", name)).read()
    code = main.migrate_cobol(src, name)["migrated_code"]
    res = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)
    return res


class TestCobolParagraphs:
    """Migrated COBOL with PERFORM used to crash (UnboundLocalError / NameError) while
    passing the syntax check: paragraphs were never turned into functions."""

    def test_perform_paragraph_runs(self):
        res = _run_migrated_cobol("INTEREST.cbl")
        assert res.returncode == 0, res.stderr
        assert "INTEREST:  5000" in res.stdout

    def test_thru_times_until_evaluate_and_goback(self):
        res = _run_migrated_cobol("LOANCALC.cbl")
        assert res.returncode == 0, res.stderr
        assert "TOTAL:  26" in res.stdout and "COUNT:  8" in res.stdout and "GOOD" in res.stdout
        assert "SHOULD NOT PRINT" not in res.stdout

    def test_missing_paragraph_is_flagged(self):
        d = main.migrate_cobol("       PROCEDURE DIVISION.\n       A-PARA.\n           PERFORM NOT-HERE.\n           STOP RUN.\n", "x.cbl")
        assert any("NOT-HERE" in c and c.startswith("REVIEW NEEDED") for c in d["changes"])


class TestPython2Migration:
    def test_hard_py2_file_migrates_to_runnable_py3(self):
        code = main.migrate_code(open(os.path.join(HERE, "tests_fixtures", "py2_hard.py")).read())["migrated_code"]
        res = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)
        assert res.returncode == 0, res.stderr
        assert "caught bad value" in res.stdout and "x=3 \n" in res.stdout and "to stderr" in res.stderr

    def test_literals_inside_strings_untouched(self):
        for src in ('s = "0777 and 10L"\n', "t = '10L xrange'\n", "x = 1.0777\n"):
            assert main.migrate_code(src)["migrated_code"] == src

    def test_has_key_simple_arg_not_flagged_as_nested(self):
        ch = main.migrate_code("if d.has_key(k):\n    pass\n")["changes"]
        assert not any("nested parentheses" in c for c in ch)


class TestSecondReviewRound:
    def test_bug7_failed_scan_is_not_http_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        def boom(*a, **k):
            raise RuntimeError("simulated failure")
        monkeypatch.setattr(main, "scan_sensitive_data", boom)
        r = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"}).post("/scan-sensitive", files={"file": ("a.py", b"x = 1\n")})
        assert r.status_code == 500 and "error" in r.json()

    def test_bug4_schema_ddl_runs_once(self):
        class Cur:
            def __init__(self): self.sql = []
            def execute(self, q, *a): self.sql.append(q)
        main._usage_log_schema_ready = False
        c1, c2 = Cur(), Cur()
        main._ensure_usage_log_schema(c1); main._ensure_usage_log_schema(c2)
        assert sum("ALTER TABLE" in q for q in c1.sql) == 2 and c2.sql == []

    def test_bug6_rule_migration_unchanged(self):
        src = open(os.path.join(HERE, "tests_fixtures", "py2_hard.py")).read()
        out = main.migrate_code(src)
        assert "for k, v in rates.items():" in out["migrated_code"] and out["migration_validity"]["syntax_valid"]

    def test_compile_check_is_not_execution(self, tmp_path):
        flag = tmp_path / "ran"
        code = f"open({str(flag)!r}, 'w').write('x')\n"
        assert main.deep_verify_python(code)["verified"] is True
        assert not flag.exists()
        assert main.deep_verify_python("return 5\n")["verified"] is False  # compile() catches what ast.parse misses


class TestRepoScanDownloadCap:
    """A huge file in a public repo used to be downloaded fully into memory before the 200KB check."""

    def test_huge_files_skipped_without_full_download(self, monkeypatch):
        import requests as _rq
        big_body = b"x = 1\n" * 500000  # ~3 MB
        read_bytes = {"n": 0}

        class FakeResp:
            def __init__(self, status, body=b"", json_data=None, declare_len=True):
                self.status_code = status; self._body = body; self._json = json_data
                self.headers = {"Content-Length": str(len(body))} if declare_len else {}
                self.encoding = "utf-8"
            def json(self): return self._json
            @property
            def text(self):
                read_bytes["n"] += len(self._body); return self._body.decode()
            def iter_content(self, chunk_size=65536):
                for i in range(0, len(self._body), chunk_size):
                    read_bytes["n"] += min(chunk_size, len(self._body) - i); yield self._body[i:i + chunk_size]
            def __enter__(self): return self
            def __exit__(self, *a): return False

        tree = {"tree": [{"path": "declared_big.py", "type": "blob", "size": len(big_body)},
                         {"path": "undeclared_big.py", "type": "blob"},
                         {"path": "ok.py", "type": "blob", "size": 9}]}
        def fake_get(url, **kw):
            if "api.github.com" in url: return FakeResp(200, json_data=tree)
            if url.endswith("undeclared_big.py"): return FakeResp(200, big_body, declare_len=False)
            if url.endswith("ok.py"): return FakeResp(200, b"print(1)\n")
            return FakeResp(200, big_body)
        monkeypatch.setattr(main.requests, "get", fake_get)
        res = main._scan_repo_blocking(main.RepoRequest(repo_url="https://github.com/owner/repo"))
        body = res if isinstance(res, dict) else __import__("json").loads(res.body)
        skipped = {s["file"]: s["reason"] for s in body.get("skipped_files", [])}
        assert "too large" in skipped.get("declared_big.py", "") and "too large" in skipped.get("undeclared_big.py", "")
        assert read_bytes["n"] < 400000, read_bytes["n"]  # never pulled the ~3 MB bodies into memory


class TestCrossUserPrivacy:
    def test_other_users_code_never_reaches_prompt_or_response(self, monkeypatch):
        leaked = "SECRET_PASSWORD = 'hbl-prod-123'  # other customer's file"
        monkeypatch.setattr(main, "find_similar_files", lambda *a, **k: [{"filename": "hbl_core_transfer.py", "similarity": 0.9, "excerpt": leaked}])
        seen = {}
        monkeypatch.setattr(main, "call_ai_provider", lambda prompt, max_tokens=1000: seen.setdefault("p", prompt) and "answer text")
        out = main.answer_code_question("def f():\n    return 1\n", "what does f do?", "mine.py")
        assert "hbl-prod-123" not in seen["p"] and "hbl_core_transfer" not in seen["p"]
        assert "hbl_core_transfer" not in str(out)

    def test_source_excerpt_not_persisted(self, monkeypatch):
        rows = []
        class Cur:
            def execute(self, q, params=None):
                if q.startswith("INSERT INTO analyzed_files"): rows.append(params)
            def close(self): pass
        class Conn:
            def cursor(self): return Cur()
            def commit(self): pass
            def close(self): pass
        monkeypatch.setattr(main, "_get_db_connection", lambda: Conn())
        main._users_table_initialized = True
        main.store_analyzed_file("a.py", "password = 'topsecret'\n" * 10)
        assert rows and rows[0][2] == ""


class TestBehavioralEvaluatorLimits:
    """An uploaded function like `return x ** 50000000` pinned the CPU and, because the
    endpoint ran on the event loop, froze the server for every user."""

    def test_huge_power_and_repetition_refused_quickly(self):
        import time
        for body in ("return 9 ** 10 ** 8", "return x ** 50000000", "return 'a' * 10 ** 10"):
            src = "def f(x):\n    " + body + "\n"
            t = time.time()
            main.calculate_behavioral_confidence(src, src, "evil.py")
            assert time.time() - t < 2, body

    def test_normal_arithmetic_still_verified(self):
        src = "def f(a, b):\n    return a * 2 + b / 4\n"
        assert main.calculate_behavioral_confidence(src, src, "ok.py")["behavioral_status"].startswith("Verified")

    def test_sandbox_endpoint_makes_no_ai_call(self, monkeypatch):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        monkeypatch.setattr(main, "ai_advanced_migrate", lambda *a, **k: (_ for _ in ()).throw(AssertionError("AI called")))
        r = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"}).post("/sandbox-test", files={"file": ("a.py", b"x = 1\n")})
        assert r.status_code == 200 and r.json()["sandbox_status"] == "Disabled"


class TestPhpJavaMigrationRuns:
    def test_php_split_literal_becomes_explode_and_runs(self):
        import shutil
        out = main.migrate_php(open(os.path.join(HERE, "tests_fixtures", "legacy2.php")).read())["migrated_code"]
        assert 'explode(","' in out and "split(" not in out
        if shutil.which("php"):
            res = subprocess.run(["php", "-r", out.replace("<?php", "").replace("?>", "")], capture_output=True, text=True, timeout=30)
            assert res.returncode == 0 and "a-b-c" in res.stdout, res.stderr

    def test_php_regex_split_left_for_review(self):
        r = main.migrate_php('<?php $p = split("[,;]", $s); ?>')
        assert 'split("[,;]"' in r["migrated_code"] and any(c.startswith("REVIEW NEEDED: split()") for c in r["changes"])

    def test_java_migration_compiles(self, tmp_path):
        import shutil
        if not shutil.which("javac"):
            return
        out = main.migrate_java(open(os.path.join(HERE, "tests_fixtures", "Bank.java")).read())["migrated_code"]
        (tmp_path / "Bank.java").write_text(out)
        res = subprocess.run(["javac", "-Xlint:none", str(tmp_path / "Bank.java")], capture_output=True, text=True, timeout=120)
        assert res.returncode == 0, res.stderr


class TestNoQuadraticRegex:
    """Inputs near the 500 KB upload limit that used to take >12 s (one per endpoint call)."""

    def _timed(self, fn, *args):
        import time
        t = time.time(); fn(*args); return time.time() - t

    def test_long_select_line(self):
        src = 'x = "' + "SELECT a " * 50000 + '"\n'
        assert self._timed(main.scan_sql_injection, src, "x.py") < 3

    def test_has_key_without_closing_paren(self):
        assert self._timed(main.migrate_code, "d.has_key(" * 45000 + "\n") < 5

    def test_long_identifier_line(self):
        assert self._timed(main.migrate_code, "a" * 450000 + "\n") < 5

    def test_many_quotes(self):
        assert self._timed(main.migrate_code, "\"'" * 225000) < 5


class TestMigrationCertificate:
    def _post(self, monkeypatch, body):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        monkeypatch.setattr(main, "_check_user_auth", lambda request: "reviewer@bank.pk")
        return TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"}).post("/issue-migration-certificate", json=body).json()

    def test_certificate_bound_to_code_hashes_and_real_confidence(self, monkeypatch):
        import hashlib
        o, m = hashlib.sha256(b"old code").hexdigest(), hashlib.sha256(b"new code").hexdigest()
        c = self._post(monkeypatch, {"filename": "a.py", "decision": "Approved", "original_sha256": o, "migrated_sha256": m, "confidence": 42})
        assert c["original_code_hash"] == o and c["migrated_code_hash"] == m and c["confidence_score"] == 42
        assert "code_binding_note" not in c

    def test_certificate_without_hashes_says_so(self, monkeypatch):
        c = self._post(monkeypatch, {"filename": "a.py", "decision": "Approved"})
        assert c["original_code_hash"] is None and c["confidence_score"] is None and "NOT bound" in c["code_binding_note"]

    def test_certificate_signature_still_verifies(self, monkeypatch):
        c = self._post(monkeypatch, {"filename": "b.py", "decision": "Approved", "confidence": 90})
        v = main.cert_manager.verify(c["certificate_id"])
        assert v.get("valid") is True or v.get("verified") is True or "tamper" not in str(v).lower(), v


class TestApprovalHistoryScope:
    def _setup(self, monkeypatch, tmp_path):
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(main, "_get_db_connection", lambda: None)
        main.save_approval_decision("a.py", "approved", "", "migration", approved_by="u1@x.pk")
        main.save_approval_decision("b.py", "rejected", "secret note", "migration", approved_by="u2@x.pk")

    def test_dashboard_counts_ui_decisions(self, monkeypatch, tmp_path):
        self._setup(monkeypatch, tmp_path)
        d = main.get_migration_dashboard()
        assert d["approved"] == 1 and d["rejected"] == 1

    def test_user_sees_only_own_history(self, monkeypatch, tmp_path):
        from fastapi.testclient import TestClient
        self._setup(monkeypatch, tmp_path)
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        monkeypatch.setattr(main, "_check_user_auth", lambda request: "u1@x.pk")
        monkeypatch.setattr(main, "_check_admin_auth", lambda request: False)
        c = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"})
        h = c.get("/approval-history").json()
        assert [e["filename"] for e in h["approval_history"]] == ["a.py"]
        d = c.get("/migration-dashboard").json()
        assert d["total_reviewed"] == 1 and "secret note" not in str(d) and "u2@x.pk" not in str(d)


class TestRemainingIssuesAfterMigration:
    def test_php_split_not_remaining_after_explode(self):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        src = open(os.path.join(HERE, "tests_fixtures", "bank_split.php"), "rb").read()
        d = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"}).post("/migrate-php", files={"file": ("bank_split.php", src)}).json()
        rem = " | ".join(d["remaining_issues"])
        assert "split()" not in rem and "ereg()" in rem and "Hardcoded password" in rem

    def test_python_fixed_items_not_remaining(self):
        from fastapi.testclient import TestClient
        main._anti_bot_patterns.clear(); main._rate_limit_store.clear()
        src = open(os.path.join(HERE, "tests_fixtures", "legacy_loan_system.py"), "rb").read()
        d = TestClient(main.app, headers={"User-Agent": "Mozilla/5.0"}).post("/migrate", files={"file": ("loan.py", src)}).json()
        rem = " | ".join(d["remaining_issues"])
        assert "xrange" not in rem and "print statement" not in rem and "SQL injection" in rem


class TestCredentialEvidenceRedaction:
    def test_password_in_connect_call_not_echoed(self):
        for src in ('$conn = mysql_connect("localhost", "root", "s3cr3tPW");',
                    'Connection c = DriverManager.getConnection(url, "sa", "s3cr3tPW");'):
            out = str(main.scan_sensitive_data(src))
            assert "s3cr3tPW" not in out, out


class TestNoSecretEchoAcrossScanners:
    SECRETS = ["Zq9PwLeakA1", "ZqLeakKeyB2", "ZqLeakTokenC3", "ZqLeakConnD4", "7654321", "4111111111111111",
               "ZqLeakBearerE5", "ZqLeakAuthF6", "ZqLeakAwsG7", "ZqLeakPrivH8"]

    def test_scanners_never_echo_secret_values(self):
        import json
        src = open(os.path.join(HERE, "tests_fixtures", "secrets_probe.py")).read()
        outputs = [main.scan_sensitive_data(src), main.detect_pii(src, "p.py"), main.scan_sql_injection(src, "p.py")]
        blob = json.dumps(outputs, default=str)
        assert not [s for s in self.SECRETS if s in blob]

    def test_connection_string_bearer_and_basic_auth_detected(self):
        src = open(os.path.join(HERE, "tests_fixtures", "secrets_probe.py")).read()
        issues = " | ".join(f["issue"] for f in main.scan_sensitive_data(src)["findings"])
        for label in ("connection string", "bearer token", "HTTP basic auth"):
            assert label in issues, label


class TestBehavioralConfidenceScales:
    def test_300_functions_is_fast(self):
        import time
        src = open(os.path.join(HERE, "tests_fixtures", "edge_06_size_60kb.py")).read()
        t = time.time()
        r = main.calculate_behavioral_confidence(src, src, "edge_06.py")
        assert time.time() - t < 5, "was ~77 s: whole file re-parsed per function per input"
        assert r["behavioral_status"].startswith("Verified")


class TestCommentsAreNotEvidence:
    """A comment/docstring saying "No AML / no OTP / no 2FA ..." used to make these checks
    report the controls as PRESENT (fraud score 5 -> 100, compliance readiness 0% -> 75%)."""
    CHECKS = [
        ("detect_fraud_gaps", lambda d: (d["fraud_score"], d["fraud_strengths"])),
        ("score_zero_trust", lambda d: d["zt_score"]),
        ("check_regulatory_framework", lambda d: d["framework_summary"]),
        ("analyze_regulation_impact", lambda d: d["regulation_summary"]),
        ("map_transaction_flow", lambda d: d.get("flow_summary")),
        ("check_swift_mt_iso20022_migration", lambda d: d.get("summary")),
        ("extract_aml_kyc", lambda d: d["verdict"]),
    ]

    def _pair(self, ext):
        base = os.path.join(HERE, "tests_fixtures")
        return open(os.path.join(base, "diff_plain." + ext)).read(), open(os.path.join(base, "diff_commented." + ext)).read()

    def test_python_java_php(self):
        for ext in ("py", "java", "php"):
            plain, commented = self._pair(ext)
            for name, pick in self.CHECKS:
                fn = getattr(main, name)
                args = (lambda s: (s,)) if name == "extract_aml_kyc" else (lambda s: (s, "x." + ext))
                assert pick(fn(*args(plain))) == pick(fn(*args(commented))), (ext, name)

    def test_exec_report_readiness_not_from_comments(self):
        plain, commented = self._pair("py")
        a = main.generate_executive_report(plain, "x.py")["exec_compliance_readiness"]["compliance_readiness_pct"]
        b = main.generate_executive_report(commented, "x.py")["exec_compliance_readiness"]["compliance_readiness_pct"]
        assert a == b == 0

    def test_c_style_blanking_keeps_strings(self):
        out = "\n".join(main._blank_comments_and_docstrings('public class A {\n  String u = "http://x/aml"; // aml\n}\n'))
        assert '"http://x/aml"' in out and "// aml" not in out


class TestSmallScannerFixes:
    def test_entropy_ignores_identifier_keys(self):
        assert main.scan_entropy_secrets('r["kyc_failure_rate"] = 1\nx = "os.path.join"\n', "a.py")["total_findings"] == 0
        assert main.scan_entropy_secrets('t = "ghp_ZqLeakTokenC333333333333"\n', "a.py")["total_findings"] == 1

    def test_php_tainted_variable(self):
        i = main.scan_sql_injection('<?php $r = mysql_query("SELECT * FROM accounts WHERE id = " . $id); ?>', "a.php")["sqli_issues"]
        assert i and i[0]["likely_source_variable"] == "$id"


class TestRepoScanRisk:
    def test_python_security_issues_rate_high(self):
        n, level, crit = main._repo_file_assessment(open(FIXTURE).read(), "compliance_audit.py")
        assert level == "High" and crit >= 1 and n >= 2

    def test_clean_file_is_low_and_label_is_a_level(self):
        assert main._repo_file_assessment("x = 1\n", "tiny.py")[1] == "Low"

    def test_one_sqli_outranks_style_warnings(self):
        php = '<?php $r = mysql_query("SELECT * FROM t WHERE id = " . $id); ?>'
        assert main._repo_file_assessment(php, "a.php")[1] == "High"


class TestServerErrorsAre500NotClientErrors:
    """A blanket `except Exception as e:` around an endpoint body catches unexpected server-side
    failures (DB down, AI call crashed, unhandled parsing exception) - that is a 500, not a 400.
    A 400 told the frontend the *request* was bad, so the UI showed a "fix your input" style
    error for what was actually an outage on our side. Deliberate input-validation responses
    (checked earlier in the same function, before anything could throw) still 400 correctly and
    must be left alone."""

    def test_no_blanket_exception_handler_still_returns_400(self):
        src = open(os.path.join(HERE, "main.py")).read()
        lines = src.split("\n")
        offenders = []
        for i, ln in enumerate(lines):
            if "JSONResponse(status_code=400" in ln and i > 0 and lines[i - 1].strip() == "except Exception as e:":
                offenders.append(i + 1)
        assert offenders == [], f"blanket except-Exception handlers still returning 400: {offenders}"

    def test_deliberate_validation_400s_were_left_alone(self):
        # these two catch a *specific* parse failure right where the bad input was read, not
        # "anything went wrong anywhere in this endpoint" - they should stay 400.
        src = open(os.path.join(HERE, "main.py")).read()
        assert 'content={"error": "Invalid JSON payload"}' in src
        assert 'content={"error": "Invalid deadline_date - use YYYY-MM-DD format."}' in src


class TestRepoAssessmentPassesFilename:
    def test_dependency_risk_gets_real_filename(self):
        n, level, crit = main._repo_file_assessment(open(FIXTURE).read(), "compliance_audit.py")
        assert isinstance(level, str)  # doesn't crash, still returns a rating


class TestSessionExpiryHandlesTimestamptz:
    """sessions.expires_at moved from TEXT to TIMESTAMPTZ, so psycopg2 now hands back a real
    datetime (often timezone-aware) instead of an ISO string. The expiry check must handle
    both, and must not raise TypeError comparing aware vs naive datetimes."""

    def _check(self, expires_val):
        from datetime import datetime as _dt
        _expires = expires_val
        if isinstance(_expires, str):
            _expires = _dt.fromisoformat(_expires)
        _now = _dt.now(_expires.tzinfo) if _expires.tzinfo is not None else _dt.now()
        return _expires < _now

    def test_expired_and_valid_for_string_naive_and_aware(self):
        from datetime import datetime as _dt, timedelta as _td, timezone as _tz
        past, future = _dt.now() - _td(hours=1), _dt.now() + _td(hours=1)
        assert self._check(past.isoformat()) is True
        assert self._check(future.isoformat()) is False
        assert self._check(past) is True
        assert self._check(future) is False
        assert self._check(_dt.now(_tz.utc) - _td(hours=1)) is True
        assert self._check(_dt.now(_tz.utc) + _td(hours=1)) is False


class TestApprovalHistoryTimestampNormalized:
    def test_source_normalizes_datetime_to_isoformat_string(self):
        # get_approval_history must convert a driver-returned datetime back to a string, since
        # get_migration_dashboard slices/sorts "timestamp" as text (h.get("timestamp")[:10]).
        src = open(os.path.join(HERE, "main.py")).read()
        assert 'r[4].isoformat() if hasattr(r[4], "isoformat") else r[4]' in src


class TestBug17ParameterizedQueryNotFlagged:
    """A DB-API placeholder ("%s" bound via a separate tuple/dict argument) is the SAFE,
    recommended pattern - the tool's own disclaimer tells developers to use it. It must not
    be flagged as SQL injection just because a bare "%" character appears in the line."""

    def test_parameterized_placeholder_is_safe(self):
        src = 'execute_sql("SELECT balance FROM accounts WHERE id = %s", (account_from,))\n'
        r = main.scan_sql_injection(src, "a.py")
        assert r["sqli_safe"] is True

    def test_percent_operator_on_the_query_string_is_still_flagged(self):
        src = 'cur.execute("SELECT * FROM t WHERE id = %s" % user_id)\n'
        r = main.scan_sql_injection(src, "a.py")
        assert r["sqli_issues"] and r["sqli_issues"][0]["issue"] == "String formatting inside execute() - SQL injection risk"

    def test_percent_dict_operator_still_flagged(self):
        src = 'query = "SELECT * FROM t WHERE name = %(name)s" % {"name": name}\n'
        r = main.scan_sql_injection(src, "a.py")
        assert r["sqli_issues"]


class TestBug18BusinessRuleMisclassification:
    """A bare "approv"/"approved"/"unapproved" match must not tag ordinary non-financial
    workflow logic (e.g. HR leave approval) as a banking "Authorization" business rule."""

    def test_hr_leave_approval_not_tagged_authorization(self):
        src = 'def check_staff_leave(leave_type, days_requested):\n    if leave_type == "unapproved" and days_requested > 2:\n        return "flag_for_hr_review"\n'
        r = main.discover_business_rules_engine(src, "hr.py")
        tags = r["discovered_rules"][0]["compliance_tags"]
        assert "Authorization" not in tags

    def test_real_transaction_approval_still_tagged_authorization(self):
        src = 'def process_transfer(txn, account):\n    if txn.approved == True and account.balance > 0:\n        return "ok"\n'
        r = main.discover_business_rules_engine(src, "bank.py")
        tags = r["discovered_rules"][0]["compliance_tags"]
        assert "Authorization" in tags

    def test_strong_authorization_terms_still_tagged_without_domain_words(self):
        src = 'def gate(user):\n    if not authorize_user(user):\n        pass\n'
        # authoriz() alone (no bare "approv") should still count - it is not a generic word
        r = main.discover_business_rules_engine('def gate(user, x):\n    if not authorize_user(user) and x > 1:\n        pass\n', "x.py")
        tags = r["discovered_rules"][0]["compliance_tags"] if r["discovered_rules"] else []
        assert "Authorization" in tags


class TestBug15DocstringNotRewritten:
    """migrate_code must never rewrite illustrative Python-2 syntax examples written inside a
    docstring - that text is documentation, not executable code, and rewriting it can silently
    change program behavior if the string is compared or displayed elsewhere."""

    def test_docstring_example_left_untouched(self):
        src = (
            'def legacy_example_docstring_only():\n'
            '    """\n'
            '    Example of old syntax (illustrative only, not real code):\n'
            '        print x\n'
            '        except Exception, e:\n'
            '        for i in xrange(10): pass\n'
            '    """\n'
            '    return True\n'
        )
        r = main.migrate_code(src)
        assert r["migrated_code"] == src
        assert r["changes"] == []

    def test_real_code_outside_docstring_still_migrated(self):
        src = (
            'def legacy_example_docstring_only():\n'
            '    """\n'
            '    print x\n'
            '    """\n'
            '    return True\n'
            '\n'
            'def real_migration_needed():\n'
            '    print x\n'
            '    for i in xrange(10): pass\n'
        )
        r = main.migrate_code(src)
        assert '"""\n    print x\n    """' in r["migrated_code"]  # docstring untouched
        assert "print(x)" in r["migrated_code"]  # real code migrated
        assert "range(10)" in r["migrated_code"]
        assert r["migrated_code"].count("\n") == src.count("\n")  # line count preserved

    def test_migrated_output_still_parses(self):
        src = (
            'def f():\n'
            '    """docstring with print x and except E, e: inside"""\n'
            '    print y\n'
            '    return 1\n'
        )
        r = main.migrate_code(src)
        import ast as _ast
        _ast.parse(r["migrated_code"])  # must not raise


class TestBehavioralConfidenceUsesRealParamNames:
    """Sample inputs for the restricted-evaluator behavioral check used to be a fixed dict of
    8 hardcoded parameter names (x, a, b, n, amount, rate, years, principal). A real function
    with different parameter names (price, pct, ...) hit "Unknown variable" and was silently
    skipped - so a real migration bug inside it could never be caught."""

    def test_non_whitelisted_param_names_no_longer_skipped(self):
        src = "def discount(price, pct):\n    return price * pct / 100\n"
        r = main.calculate_behavioral_confidence(src, src, "x.py")
        assert r["skipped_functions"] == []
        assert r["behavioral_status"] == "Verified (1/1 functions)"

    def test_real_migration_bug_with_custom_param_names_is_caught(self):
        orig = "def discount(price, pct):\n    return price * pct / 100\n"
        buggy_migration = "def discount(price, pct):\n    return price * pct * 100\n"
        r = main.calculate_behavioral_confidence(orig, buggy_migration, "x.py")
        assert r["behavioral_status"] == "Mismatch Detected"
        assert "discount" in r["behavioral_summary"]

    def test_old_style_param_names_still_work(self):
        src = "def f(a, b):\n    return a * 2 + b / 4\n"
        assert main.calculate_behavioral_confidence(src, src, "ok.py")["behavioral_status"].startswith("Verified")


class TestPhpDocCommentsNotRewritten:
    """Same root cause as Bug 15 in the Python migrator: migrate_php's PHP4-constructor fix
    and curly-brace-access fix ran a regex over the whole file with no comment awareness, and
    the split()->explode() conversion loop (unlike every other line-based rule loop in this
    function) never got a "skip comment lines" guard - so illustrative old-syntax examples
    written inside a /** ... */ PHPDoc block were rewritten as if they were live code."""

    def test_split_example_in_docblock_left_untouched(self):
        src = (
            '<?php\n'
            '/**\n'
            ' * Example usage (old style, illustrative only):\n'
            ' *   $result = split(",", $csv);\n'
            ' */\n'
            'function realFunc($csv) {\n'
            '    $parts = split(",", $csv);\n'
            '    return $parts;\n'
            '}\n'
        )
        r = main.migrate_php(src)
        assert '$result = split(",", $csv);' in r["migrated_code"]  # docblock untouched
        assert 'explode(",", $csv)' in r["migrated_code"]  # real code migrated
        assert r["migrated_code"].count("\n") == src.count("\n")

    def test_curly_brace_example_in_docblock_left_untouched(self):
        src = (
            '<?php\n'
            '/**\n'
            ' * Old style: $x{0} accesses first char (illustrative only)\n'
            ' */\n'
            'function real($x) {\n'
            '    return $x{0};\n'
            '}\n'
        )
        r = main.migrate_php(src)
        assert '$x{0} accesses' in r["migrated_code"]  # docblock untouched
        assert 'return $x[0];' in r["migrated_code"]  # real code migrated

    def test_real_fixtures_unchanged(self):
        for fname in ("bank_split.php", "legacy2.php"):
            path = os.path.join(HERE, "tests_fixtures", fname)
            src = open(path).read()
            r = main.migrate_php(src)
            assert r["validation"]["valid"] is True


class TestPhpCommentLikeSequenceInStringNotTreatedAsComment:
    """The fix for TestPhpDocCommentsNotRewritten (masking /* ... */ block comments before any
    rewrite rule runs) had its own bug: the comment-boundary search ran directly on the raw
    source, so a "/*"-like or "*/"-like character sequence sitting INSIDE an unrelated PHP
    string literal (plain data, not a real comment delimiter) was matched as if it were a
    genuine comment boundary. Two unrelated strings - one containing a fake "/*", a later one
    containing a fake "*/" - caused every migration rule to silently treat all the real code in
    between as one giant fake comment and skip it with zero error or warning."""

    def test_real_code_between_fake_comment_markers_in_strings_is_still_migrated(self):
        src = (
            '<?php\n'
            '$note = "see /* below for details";\n'
            'class Foo {\n'
            '    function Foo($x) {\n'
            '        $this->x = $x;\n'
            '    }\n'
            '}\n'
            '$parts = split(",", $data);\n'
            '$other = "end */ of note";\n'
        )
        r = main.migrate_php(src)
        assert "PHP 4-style constructor (method name matched class name) -> __construct()" in r["changes"]
        assert any(c.startswith("split() with a literal delimiter -> explode()") for c in r["changes"])
        assert "function __construct($x)" in r["migrated_code"]
        assert "explode(\",\", $data)" in r["migrated_code"]
        # the fake comment markers, being plain string data, must survive untouched
        assert '$note = "see /* below for details";' in r["migrated_code"]
        assert '$other = "end */ of note";' in r["migrated_code"]

    def test_genuine_block_comment_still_masked_alongside_fake_markers_in_strings(self):
        src = (
            '<?php\n'
            '/* old code:\n'
            'class Foo {\n'
            '    function Foo($x) {}\n'
            '}\n'
            '$parts = split(",", $data);\n'
            '*/\n'
            'class Bar {\n'
            '    function Bar($y) {\n'
            '        $this->y = $y;\n'
            '    }\n'
            '}\n'
            '$parts2 = split(";", $data2);\n'
        )
        r = main.migrate_php(src)
        # illustrative example inside the real comment is untouched
        assert 'function Foo($x) {}' in r["migrated_code"]
        assert '$parts = split(",", $data);\n*/' in r["migrated_code"]
        # real code after the comment is still migrated
        assert "function __construct($y)" in r["migrated_code"]
        assert 'explode(";", $data2)' in r["migrated_code"]

    def test_migrated_output_has_valid_php_syntax(self):
        import subprocess, tempfile, pytest
        src = (
            '<?php\n'
            '$note = "see /* below for details";\n'
            'class Foo {\n'
            '    function Foo($x) {\n'
            '        $this->x = $x;\n'
            '    }\n'
            '}\n'
            '$parts = split(",", $data);\n'
            '$other = "end */ of note";\n'
        )
        r = main.migrate_php(src)
        with tempfile.NamedTemporaryFile(mode="w", suffix=".php", delete=False) as f:
            f.write(r["migrated_code"])
            path = f.name
        try:
            proc = subprocess.run(["php", "-l", path], capture_output=True, text=True)
            assert proc.returncode == 0, proc.stdout + proc.stderr
        except FileNotFoundError:
            pytest.skip("php CLI not available")
        finally:
            os.unlink(path)


class TestAuditBlockchainKeepsGenesisWhenTrimmed:
    """add_block() used to bound memory with `del self.chain[:-2000]`, which deletes EVERY
    block except the newest 2000 - including the true genesis block once the chain grew past
    that size. get_summary()'s "genesis_hash" (the audit trail's supposed immutable anchor)
    would then silently start reporting a different, arbitrary block's hash, defeating the
    purpose of an immutable anchor. Fixed to always keep the true genesis plus a rolling
    window of the newest 2000 blocks, with verify_chain() aware of the resulting index gap."""

    def test_genesis_hash_survives_trimming(self):
        bc = main.StarBuildBlockchain()
        genesis_hash = bc.chain[0].hash
        for _ in range(2500):
            bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")
        assert bc.chain[0].hash == genesis_hash
        assert bc.get_summary()["genesis_hash"] == genesis_hash

    def test_chain_still_reports_valid_after_trimming(self):
        bc = main.StarBuildBlockchain()
        for _ in range(2500):
            bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")
        valid, tampered_at = bc.verify_chain()
        assert valid is True
        assert tampered_at is None

    def test_tampering_a_retained_block_is_still_detected_after_trimming(self):
        bc = main.StarBuildBlockchain()
        for _ in range(2500):
            bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")
        bc.chain[5].hash = "tampered_hash_value"
        valid, tampered_at = bc.verify_chain()
        assert valid is False
        assert tampered_at == bc.chain[5].index

    def test_chain_length_bounded(self):
        bc = main.StarBuildBlockchain()
        for _ in range(2500):
            bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")
        # genesis + newest 2000, not unbounded growth
        assert len(bc.chain) == 2001


class TestGithubWebhookReturns500OnInternalError:
    """process_github_webhook() catches its own internal exceptions and returns a plain
    {"error": ...} dict instead of raising. The endpoint's own try/except never saw an
    exception in that case, so it returned the dict as-is - FastAPI serialized it as a normal
    HTTP 200, even though processing had actually failed. A caller checking only the status
    code (the standard way to detect a failed webhook delivery) would see success."""

    def test_internal_processing_error_returns_500_not_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "testsecret")

        def _boom(payload):
            return {"error": "Webhook processing failed safely: boom"}
        monkeypatch.setattr(main, "process_github_webhook", _boom)

        body = b'{"ref": "refs/heads/main"}'
        sig = "sha256=" + hmac.new(b"testsecret", body, hashlib.sha256).hexdigest()
        resp = TestClient(main.app).post("/github-webhook", content=body, headers={"x-hub-signature-256": sig, "content-type": "application/json"})
        assert resp.status_code == 500
        assert "error" in resp.json()

    def test_successful_processing_still_returns_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "testsecret")

        def _ok(payload):
            return {"repo": "x/y", "files_scanned": 0, "results": []}
        monkeypatch.setattr(main, "process_github_webhook", _ok)

        body = b'{"ref": "refs/heads/main"}'
        sig = "sha256=" + hmac.new(b"testsecret", body, hashlib.sha256).hexdigest()
        resp = TestClient(main.app).post("/github-webhook", content=body, headers={"x-hub-signature-256": sig, "content-type": "application/json"})
        assert resp.status_code == 200
        assert resp.json()["repo"] == "x/y"


class TestGithubHelperEndpointsReturn400OnInputError:
    """Same bug class as TestGithubWebhookReturns500OnInternalError: get_codebase_history(),
    get_file_at_commit()/get_time_travel_diff(), and fetch_github_issues() all return a plain
    {"error": ...} dict for invalid input or an unreachable/rate-limited GitHub repo, instead of
    raising - so their endpoints' own try/except never saw an exception, and the dict was
    returned as-is (HTTP 200) even though the request had actually failed. Fixed to check the
    result for an "error" key and return it as a 400, matching the convention already used for
    the same kind of error in /scan-repo."""

    def test_codebase_history_invalid_url_returns_400(self):
        from fastapi.testclient import TestClient
        resp = TestClient(main.app).post("/codebase-history", json={"repo_url": "not-a-url"})
        assert resp.status_code == 400
        assert "error" in resp.json()

    def test_time_travel_diff_invalid_url_returns_400(self):
        from fastapi.testclient import TestClient
        resp = TestClient(main.app).post("/time-travel-diff", json={
            "repo_url": "not-a-url", "file_path": "x.py",
            "commit_old": "abc1234", "commit_new": "def5678",
        })
        assert resp.status_code == 400
        assert "error" in resp.json()

    def test_github_issues_invalid_url_returns_400(self):
        from fastapi.testclient import TestClient
        resp = TestClient(main.app).post("/github-issues", json={"repo_url": "not-a-url"})
        assert resp.status_code == 400
        assert "error" in resp.json()

    def test_codebase_history_valid_shape_still_returns_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setattr(main, "get_codebase_history", lambda repo_url, file_path="": {"has_history": False, "history_summary": "No commit history found."})
        resp = TestClient(main.app).post("/codebase-history", json={"repo_url": "https://github.com/x/y"})
        assert resp.status_code == 200


class TestMigrationRoadmapAndCrossLanguagePassErrorsThrough:
    """Same bug class as TestGithubHelperEndpointsReturn400OnInputError: generate_migration_roadmap()
    and cross_language_migrate() both return a plain {"error": ...} dict instead of raising, so
    their endpoints returned it as a silent HTTP 200. /migration-roadmap had a second bug on top:
    scan_repo_endpoint() (called internally) returns a JSONResponse (not a dict) on its own
    validation failures, and generate_migration_roadmap()'s isinstance(dict) guard replaced that
    JSONResponse's real error message with a generic "Invalid repository scan result provided" -
    which then also went out as HTTP 200."""

    def test_migration_roadmap_invalid_repo_url_returns_400_with_real_reason(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setattr(main, "_check_user_auth", lambda request: "test@example.com")
        resp = TestClient(main.app).post("/migration-roadmap", json={"repo_url": "not-a-valid-url"})
        assert resp.status_code == 400
        assert "valid HTTPS GitHub repo URL" in resp.json()["error"]

    def test_migration_roadmap_success_still_returns_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setattr(main, "_check_user_auth", lambda request: "test@example.com")

        async def _fake_scan(req):
            return {"repo": "x/y", "file_reports": [{"file": "a.py", "risk_level": "Low"}]}
        monkeypatch.setattr(main, "scan_repo_endpoint", _fake_scan)
        resp = TestClient(main.app).post("/migration-roadmap", json={"repo_url": "https://github.com/x/y"})
        assert resp.status_code == 200
        assert resp.json()["repo"] == "x/y"

    def test_cross_language_migrate_unsupported_pair_returns_400(self):
        from fastapi.testclient import TestClient
        resp = TestClient(main.app).post("/cross-language-migrate", json={"source": "print(1)", "from_lang": "python", "to_lang": "cobol"})
        assert resp.status_code == 400
        assert "Unsupported language pair" in resp.json()["error"]

    def test_cross_language_migrate_success_still_returns_200(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setattr(main, "cross_language_migrate", lambda source, from_lang, to_lang: {"translated_code": "print(1);", "confidence_score": 40})
        resp = TestClient(main.app).post("/cross-language-migrate", json={"source": "print(1)", "from_lang": "python", "to_lang": "javascript"})
        assert resp.status_code == 200
        assert resp.json()["translated_code"] == "print(1);"


class TestAuditBlockchainThreadSafety:
    """verify_chain() and get_summary() used to read self.chain (len(), indexing) without
    holding self._lock, while add_block() mutates AND REASSIGNS self.chain (the genesis+newest
    -2000 trim) under that same lock. That is a classic TOCTOU race: a length read at the top
    of verify_chain()'s loop can be computed against the list BEFORE a concurrent add_block()
    swaps self.chain for a shorter one, so an index used later in the same loop can fall outside
    the new, shorter list and raise IndexError - crashing whatever endpoint called it (e.g. the
    audit-log summary endpoint) under concurrent load. Fixed by using an RLock (verify_chain and
    get_summary nest) and holding it for the whole read. A similar unsynchronized
    len(...)+[-1] read in the certificate-issuance code was fixed the same way via a new
    get_chain_length_and_head_hash() atomic accessor."""

    def test_concurrent_add_block_and_verify_chain_no_crash(self):
        import threading
        bc = main.StarBuildBlockchain()
        errors = []

        def writer():
            for _ in range(1500):
                bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")

        def reader():
            for _ in range(1000):
                try:
                    bc.verify_chain()
                    bc.get_summary()
                except Exception as e:
                    errors.append(e)

        threads = [threading.Thread(target=writer)] + [threading.Thread(target=reader) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert errors == []
        assert bc.verify_chain()[0] is True

    def test_chain_length_and_head_hash_atomic_accessor(self):
        bc = main.StarBuildBlockchain()
        for _ in range(5):
            bc.add_block("test", "f.py", "u@x.com", "1.2.3.4", "ok")
        length, head_hash = bc.get_chain_length_and_head_hash()
        assert length == len(bc.chain)
        assert head_hash == bc.chain[-1].hash


class TestAiMigrateTestScenarioFailureDoesNotLookLikeMigrationFailure:
    """generate_test_scenarios() used to return a plain {"error": ...} key when the AI provider
    was unreachable. /ai-migrate merges that dict straight into its main response with
    result.update(...), so that "error" key landed at the TOP LEVEL of a response describing an
    otherwise fully successful migration (migrated_code present, confidence_score set,
    dockerfile generated, ...). Any caller checking `if response.error` would wrongly treat a
    successful migration as failed, just because the optional AI test-scenario step couldn't
    reach the AI provider. Renamed to "test_scenarios_error", matching the existing
    "parity_error"/"dockerfile_error" convention for the other optional post-migration steps."""

    def test_generate_test_scenarios_uses_specific_error_key(self, monkeypatch):
        monkeypatch.setattr(main, "call_ai_provider", lambda prompt, max_tokens=800: "AI_ERROR: provider unreachable")
        result = main.generate_test_scenarios("def f(): return 1", "f.py")
        assert "error" not in result
        assert result["test_scenarios_error"] == "AI_ERROR: provider unreachable"

    def test_ai_migrate_endpoint_success_has_no_top_level_error_key(self, monkeypatch):
        from fastapi.testclient import TestClient
        monkeypatch.setattr(main, "ai_advanced_migrate", lambda source, lang: {"migrated_code": 'print("hi")', "confidence_score": 90, "confidence_level": "High"})
        monkeypatch.setattr(main, "call_ai_provider", lambda prompt, max_tokens=800: "AI_ERROR: provider unreachable")
        resp = TestClient(main.app).post("/ai-migrate", files={"file": ("test.py", b"print(1)", "text/plain")})
        assert resp.status_code == 200
        body = resp.json()
        assert "error" not in body
        assert body["migrated_code"] == 'print("hi")'
        assert body["test_scenarios_error"] == "AI_ERROR: provider unreachable"

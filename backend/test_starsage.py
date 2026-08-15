"""
StarSage backend regression test suite.
Covers the most critical fixes from this development session:
password security, migration correctness, ReDoS protection, and secret redaction.
Run with: pytest test_starsage.py -v
"""
import time
import main


class TestPasswordSecurity:
    def test_hash_and_verify_correct_password(self):
        h = main._hash_password("mySecurePass123")
        assert main._verify_password("mySecurePass123", h) is True

    def test_hash_and_verify_wrong_password(self):
        h = main._hash_password("mySecurePass123")
        assert main._verify_password("wrongPassword", h) is False

    def test_hash_is_salted_differently_each_time(self):
        h1 = main._hash_password("samePassword")
        h2 = main._hash_password("samePassword")
        assert h1 != h2


class TestMigrationCorrectness:
    def test_has_key_simple_case_converts_correctly(self):
        result = main.migrate_code('if d.has_key("key"):\n    pass')
        assert 'if "key" in d:' in result["migrated_code"]

    def test_has_key_nested_parens_left_unchanged_not_corrupted(self):
        original = "if d.has_key(get_key(x)):\n    pass"
        result = main.migrate_code(original)
        assert "get_key(x in d)" not in result["migrated_code"]
        assert "d.has_key(get_key(x))" in result["migrated_code"]

    def test_multi_exception_tuple_syntax_converts(self):
        code = "try:\n    pass\nexcept (IOError, OSError), e:\n    pass"
        result = main.migrate_code(code)
        assert "except (IOError, OSError) as e:" in result["migrated_code"]
        assert result["migration_validity"]["syntax_valid"] is True

    def test_chevron_print_flagged_as_syntax_invalid(self):
        code = 'print >>sys.stderr, "test"'
        result = main.migrate_code(code)
        assert result["migration_validity"]["syntax_valid"] is False


class TestSecretRedaction:
    def test_hardcoded_password_evidence_is_redacted(self):
        code = 'password = "supersecret123"'
        result = main.scan_sensitive_data(code)
        for finding in result["findings"]:
            assert "supersecret123" not in finding["evidence"]

    def test_pii_evidence_is_redacted(self):
        code = 'password = "secret123"'
        result = main.detect_pii(code, "test.py")
        for finding in result["pii_findings"]:
            assert "secret123" not in finding.get("evidence", "")


class TestReDoSProtection:
    def test_long_line_does_not_cause_catastrophic_backtracking(self):
        malicious_input = 'x = "' + ("a" * 80000) + '"'
        start = time.time()
        main.scan_sensitive_data(malicious_input)
        elapsed = time.time() - start
        assert elapsed < 2.0, f"Took {elapsed}s - possible ReDoS regression"


class TestAuthSecurity:
    def test_login_with_no_database_fails_gracefully(self):
        result = main.login_user("test@example.com", "anypassword")
        assert result["success"] is False
        assert "error" in result

    def test_register_rejects_short_password(self):
        result = main.register_user("test@example.com", "short")
        assert result["success"] is False

    def test_register_rejects_invalid_email(self):
        result = main.register_user("not-an-email", "validpassword123")
        assert result["success"] is False


class TestCodeSmells:
    def test_trivial_duplicate_lines_not_flagged(self):
        code = "def a():\n    return None\ndef b():\n    return None\n"
        result = main.detect_code_smells(code, "test.py")
        assert result["total_smells"] == 0

    def test_deep_nesting_detected_in_cobol(self):
        code = "      000010 IF X > 0\n      000020    IF Y > 0\n      000030       IF Z > 0\n      000040          DISPLAY 'x'"
        result = main.detect_code_smells(code, "test.cbl")
        assert result["total_smells"] >= 1
        assert result["code_smells"][0]["type"] == "Deep Nesting"


class TestMigrationRoadmap:
    def test_none_input_does_not_crash(self):
        result = main.generate_migration_roadmap(None)
        assert "error" in result

    def test_empty_reports_works(self):
        result = main.generate_migration_roadmap({"file_reports": []})
        assert result["total_files"] == 0
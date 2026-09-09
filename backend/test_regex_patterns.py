"""
Genuinely-decisive-regression-test-suite for the regex-word-boundary/substring-matching
bug class that has recurred 4 times this session (Structuring, CNIC/NTN, Round-Trip/Digital-Sig,
context-filters). Every _has_*_context helper and every new keyword pattern MUST be tested here
against realistic snake_case Python identifiers before being trusted in production.
"""
import main


def test_has_kyc_context_matches_snake_case_identifiers():
    assert main._has_kyc_context("def f(customer_id, kyc_data): pass") is True
    assert main._has_kyc_context("def f(onboard_step): pass") is True
    assert main._has_kyc_context("def f(nationality_code): pass") is True


def test_has_financial_context_matches_snake_case_identifiers():
    assert main._has_financial_context("def f(amount_due, account_id): pass") is True
    assert main._has_financial_context("def f(balance_after, iban_number): pass") is True


def test_has_crypto_context_matches_snake_case_identifiers():
    assert main._has_crypto_context("def f(rsa_key, hash_value): pass") is True
    assert main._has_crypto_context("def f(cert_data): pass") is True


def test_customer_risk_rating_detects_realistic_snake_case_function():
    code = "def calculate_risk_rating(customer_id, kyc_data):\n    return 'approved'"
    r = main.check_customer_risk_rating(code, "test.py")
    assert r["functions_found"] >= 1, "CRR must detect realistic snake_case KYC functions"
    assert r["total_findings"] == 1, "CRR must flag missing risk-tier logic"


def test_roundtrip_detects_realistic_snake_case_function():
    code = "def process_wire_transfer(amount_value, account_id):\n    return True"
    r = main.check_roundtrip_transaction_logic(code, "test.py")
    assert r["functions_found"] >= 1, "Round-Trip must detect realistic snake_case transfer functions"

def test_context_helpers_match_plurals_and_gerunds():
    assert main._has_kyc_context("def f(customers): pass") is True
    assert main._has_kyc_context("def f(profiles): pass") is True
    assert main._has_kyc_context("def process_customer_onboarding(): pass") is True
    assert main._has_financial_context("def f(accounts, balances): pass") is True
    assert main._has_crypto_context("def f(certificates, hashes): pass") is True

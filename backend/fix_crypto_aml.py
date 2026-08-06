with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''def scan_crypto(source):
    findings = []
    pqc_needed = False
    for pattern, label, severity, recommendation in CRYPTO_PATTERNS:
        matches = re.findall(pattern, source)
        count = len(matches)
        if count > 0:'''
new1 = '''CRYPTO_PATTERNS_COMPILED = [(re.compile(p), label, sev, rec) for p, label, sev, rec in CRYPTO_PATTERNS]

def scan_crypto(source):
    findings = []
    pqc_needed = False
    source_lines = source.split(chr(10))
    for pattern, label, severity, recommendation in CRYPTO_PATTERNS_COMPILED:
        count = 0
        line_nums = []
        for i, ln in enumerate(source_lines):
            if ln.strip().startswith(("#", "//")):
                continue
            _m = pattern.findall(ln)
            if _m:
                count += len(_m)
                line_nums.append(str(i+1))
        if count > 0:'''

old1b = '''            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "recommendation": recommendation,
                "pqc": is_pqc
            })'''
new1b = '''            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "recommendation": recommendation,
                "pqc": is_pqc
            })'''

old2 = '''def extract_aml_kyc(source):
    findings = []
    for pattern, label, category, note in AML_KYC_PATTERNS:
        matches = re.findall(pattern, source)
        count = len(matches)
        if count > 0:
            findings.append({
                "pattern": label,
                "category": category,
                "occurrences": count,
                "note": note
            })'''
new2 = '''AML_KYC_PATTERNS_COMPILED = [(re.compile(p), label, cat, note) for p, label, cat, note in AML_KYC_PATTERNS]

def extract_aml_kyc(source):
    findings = []
    source_lines = source.split(chr(10))
    for pattern, label, category, note in AML_KYC_PATTERNS_COMPILED:
        count = 0
        line_nums = []
        for i, ln in enumerate(source_lines):
            if ln.strip().startswith(("#", "//")):
                continue
            _m = pattern.findall(ln)
            if _m:
                count += len(_m)
                line_nums.append(str(i+1))
        if count > 0:
            findings.append({
                "pattern": label,
                "category": category,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "note": note
            })'''

count1 = content.count(old1)
count1b = content.count(old1b)
count2 = content.count(old2)
print("scan_crypto (part 1):", count1)
print("scan_crypto (part 2):", count1b)
print("extract_aml_kyc:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("scan_crypto part 1 PATCHED")
if count1b == 1:
    content = content.replace(old1b, new1b, 1)
    print("scan_crypto part 2 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("extract_aml_kyc PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")
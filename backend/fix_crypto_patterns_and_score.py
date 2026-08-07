with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old_patterns = '''(r"(?i)\\bDiffie[-\\s]?Hellman\\b", "Diffie-Hellman - quantum-vulnerable key exchange", "Medium", "Migrate to a PQC key-exchange (e.g. Kyber) - PQC Path"),
]'''
new_patterns = '''(r"(?i)\\bDiffie[-\\s]?Hellman\\b", "Diffie-Hellman - quantum-vulnerable key exchange", "Medium", "Migrate to a PQC key-exchange (e.g. Kyber) - PQC Path"),
    (r"(?i)\\b(Blowfish|CAST5|IDEA)\\b", "Weak cipher (Blowfish/CAST5/IDEA)", "High", "Use AES-256"),
    (r"(?i)\\bPKCS1v15\\b", "PKCS1v15 padding - vulnerable to padding-oracle attacks", "Medium", "Use OAEP padding"),
    (r"(?i)\\bSSLv[23]\\b|TLSv1\\.[01]\\b", "Deprecated SSL/TLS version", "High", "Use TLS 1.3"),
    (r"(?i)\\brandom\\.random\\(\\)", "Insecure random - not cryptographically secure", "Medium", "Use the secrets module for security-sensitive randomness"),
]'''

old_score = '''    q_score = 100
    for f in findings:
        if f.get("pqc"):
            q_score -= 20
        elif f.get("severity") == "High":
            q_score -= 15
        else:
            q_score -= 10
    if q_score < 0:
        q_score = 0'''
new_score = '''    q_score = 100.0
    for f in findings:
        if f.get("pqc"):
            q_score *= 0.85
        elif f.get("severity") == "High":
            q_score *= 0.88
        else:
            q_score *= 0.92
    q_score = round(q_score)
    if q_score < 0:
        q_score = 0'''

count_patterns = content.count(old_patterns)
count_score = content.count(old_score)
print("Patterns occurrences:", count_patterns)
print("Score occurrences:", count_score)

if count_patterns == 1:
    content = content.replace(old_patterns, new_patterns, 1)
    print("Patterns PATCHED")
if count_score == 1:
    content = content.replace(old_score, new_score, 1)
    print("Score PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")
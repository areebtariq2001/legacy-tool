with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)\\bDiffie[-\\s]?Hellman\\b", "Diffie-Hellman - quantum-vulnerable key exchange", "Medium", "PQC Path: plan post-quantum key exchange (e.g. Kyber)."),'''
new = old + '''
    (r"(?i)\\b(Blowfish|CAST5|IDEA)\\b", "Weak cipher (Blowfish/CAST5/IDEA)", "High", "Use AES-256"),
    (r"(?i)\\bPKCS1v15\\b", "PKCS1v15 padding - vulnerable to padding-oracle attacks", "Medium", "Use OAEP padding"),
    (r"(?i)\\bSSLv[23]\\b|TLSv1\\.[01]\\b", "Deprecated SSL/TLS version", "High", "Use TLS 1.3"),
    (r"(?i)\\brandom\\.random\\(\\)", "Insecure random - not cryptographically secure", "Medium", "Use the secrets module for security-sensitive randomness"),'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")
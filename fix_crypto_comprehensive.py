with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old_md5 = '''(r"(?i)\\b(MD5)\\b", "MD5 - broken hash", "High"'''
new_md5 = '''(r"(?i)\\b(hashlib\\.md5|MD5\\.new|MessageDigest\\.getInstance\\s*\\(\\s*[\\x22\\x27]MD5)", "MD5 - broken hash (actual usage)", "High"'''

old_rsa = '''(r"(?i)\\bRSA\\b", "RSA - quantum-vulnerable public-key crypto", "Medium"'''
new_rsa = '''(r"(?i)\\b(import\\s+rsa|RSA\\.(generate|import_key|construct)|from\\s+Crypto\\.PublicKey\\s+import\\s+RSA|RSA_generate_key|RSA\\.new)", "RSA - quantum-vulnerable public-key crypto (actual usage)", "Medium"'''

old_sha1 = '''(r"(?i)\\b(SHA1|SHA-1)\\b", "SHA-1 - deprecated hash", "High"'''
new_sha1 = '''(r"(?i)\\b(SHA1|SHA-1|sha1\\s*\\(|SHA1with|hashlib\\.sha1)", "SHA-1 - deprecated hash", "High"'''

count_md5 = content.count(old_md5)
count_rsa = content.count(old_rsa)
count_sha1 = content.count(old_sha1)
print("MD5 occurrences:", count_md5)
print("RSA occurrences:", count_rsa)
print("SHA1 occurrences:", count_sha1)

if count_md5 == 1:
    content = content.replace(old_md5, new_md5, 1)
    print("MD5 PATCHED")
if count_rsa == 1:
    content = content.replace(old_rsa, new_rsa, 1)
    print("RSA PATCHED")
if count_sha1 == 1:
    content = content.replace(old_sha1, new_sha1, 1)
    print("SHA1 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")
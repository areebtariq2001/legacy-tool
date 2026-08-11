import main

test_code = '''import hashlib
def hash_pwd(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()'''

result = main.scan_crypto(test_code)
for f in result["findings"]:
    print(f["issue"], "|", f["evidence"])
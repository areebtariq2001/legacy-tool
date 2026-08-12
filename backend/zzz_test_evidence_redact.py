import main

test_code = 'password = "supersecret123"\napi_key = "sk-1234567890abcdef"'
r = main.scan_sensitive_data(test_code)
for f in r["findings"]:
    print(f["issue"], "|", f["evidence"])
import main

test_code = '''password = "supersecret123"
api_key = "sk-1234567890"
os.system("rm -rf " + user_input)'''

result = main.scan_sensitive_data(test_code)
for f in result["findings"]:
    print(f["issue"], "|", f["evidence"])
import requests
code = "function hash_password($p) { return md5($p); }\nfunction check_transaction($amt) { if ($amt > 1000) { return false; } return true; }"
r = requests.post(
    'https://legacy-migration-tool-1.onrender.com/cross-language-migrate',
    json={'source': code, 'from_lang': 'php', 'to_lang': 'python'}
)
print(r.json())
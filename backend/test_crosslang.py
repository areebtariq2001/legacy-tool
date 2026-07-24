import main
code = "function hash_password($p) { return md5($p); }\nfunction check_transaction($amt) { if ($amt > 1000) { return false; } return true; }"
r = main.cross_language_migrate(code, "php", "python")
print("ERROR:", r.get("error"))
print("TRANSLATED:", r.get("translated_code"))
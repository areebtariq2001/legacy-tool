with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    hardcoded_patterns = [(r"(?i)\b\w*(password|passwd|pwd)\w*\s*=\s*[\"\x27][^\"\x27]{3,}[\"\x27]", "Hardcoded credential (password)", "CRITICAL: Never hardcode passwords - move to a secrets manager or environment variable immediately"), (r"(?i)\b\w*(_user|db_user|username)\w*\s*=\s*[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded credential (username)", "Move to environment variable (e.g. DB_USER)"), (r"(?i)(host|hostname|server)\s*=\s*[\"\x27][\w\.\-]+[\"\x27]", "Hardcoded host/server address", "Move to environment variable (e.g. DB_HOST) or a config file loaded at startup"), (r"(?i)(port)\s*=\s*\d{2,5}", "Hardcoded port number", "Move to environment variable (e.g. APP_PORT) for flexibility across environments"), (r"(?i)(debug)\s*=\s*True", "Hardcoded debug=True", "Should be environment-controlled - never run debug=True in production"), (r"(?i)(log_level)\s*=\s*[\"\x27]\w+[\"\x27]", "Hardcoded log level", "Move to environment variable (e.g. LOG_LEVEL) for environment-specific logging"), (r"(?i)(max_connections|cache_ttl|timeout)\w*\s*=\s*\d+", "Hardcoded tuning parameter", "Move to environment variable for environment-specific tuning"), (r"[\"\x27][^\"\x27]*\.(ini|cfg|conf|env)[\"\x27]", "Hardcoded config file path", "Use a config-loading library (e.g. python-dotenv, configparser) with environment-aware paths")]'''

new = old + '''
    if filename.lower().endswith((".cbl", ".cob")):
        hardcoded_patterns += [(r"(?i)[\w-]*(password|passwd|pwd)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded credential (password, COBOL VALUE clause)", "CRITICAL: Never hardcode passwords - move to a secrets manager or environment variable immediately"), (r"(?i)[\w-]*(username|user_name|db.?user)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded credential (username, COBOL VALUE clause)", "Move to environment variable (e.g. DB_USER)"), (r"(?i)[\w-]*(host|hostname|server)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded host/server address (COBOL VALUE clause)", "Move to environment variable (e.g. DB_HOST) or a config file loaded at startup")]'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
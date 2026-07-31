with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line = 409
idx = target_line - 1
print("Line at 409:", repr(lines[idx]))

insert_block = []
insert_block.append("\n")
insert_block.append("JAVA_RISK_RULES = [\n")
insert_block.append('    ("log4j", "Logging", "High", "Older Log4j versions have had serious remote-code-execution vulnerabilities (e.g. Log4Shell).", "Upgrade to Log4j 2.17.1+ or migrate to a maintained logging framework."),\n')
insert_block.append('    ("commons-collections", "Library", "High", "Older Apache Commons Collections versions are associated with known deserialization exploits.", "Upgrade to a patched version and avoid deserializing untrusted data."),\n')
insert_block.append('    ("Struts", "Framework", "High", "Apache Struts has had multiple critical remote-code-execution CVEs.", "Upgrade to the latest supported Struts version or migrate off it."),\n')
insert_block.append('    ("XMLDecoder", "Serialization", "High", "XMLDecoder can execute arbitrary code when deserializing untrusted XML.", "Avoid XMLDecoder on untrusted input; use a safe data format instead."),\n')
insert_block.append('    ("ObjectInputStream", "Serialization", "Medium", "Java native deserialization of untrusted data is a common source of RCE vulnerabilities.", "Validate/allow-list classes before deserializing, or avoid native serialization for untrusted input."),\n')
insert_block.append('    ("javax.xml", "XML", "Medium", "Default Java XML parsers can be vulnerable to XXE (XML External Entity) attacks if not configured securely.", "Disable external entity resolution explicitly when parsing untrusted XML."),\n')
insert_block.append("]\n")
insert_block.append("\n")
insert_block.append("PHP_RISK_RULES = [\n")
insert_block.append('    ("mysql_", "Database", "High", "The mysql_* extension was removed in PHP 7 and has no built-in SQL-injection protection.", "Migrate to mysqli or PDO with prepared statements."),\n')
insert_block.append('    ("eval(", "Code Execution", "High", "eval() executes arbitrary PHP code and is a common source of remote-code-execution vulnerabilities.", "Remove eval() usage; use a safer, explicit alternative for the intended logic."),\n')
insert_block.append('    ("unserialize(", "Deserialization", "High", "unserialize() on untrusted input can lead to object injection and remote code execution.", "Use json_decode() for untrusted data, or restrict allowed classes if unserialize() is required."),\n')
insert_block.append('    ("create_function", "Code Execution", "Medium", "create_function() was removed in PHP 8 and had similar risks to eval().", "Replace with an anonymous function (closure)."),\n')
insert_block.append('    ("md5(", "Cryptography", "Medium", "MD5 is not a secure hashing algorithm for passwords or security-sensitive data.", "Use password_hash() for passwords, or SHA-256+ for general hashing."),\n')
insert_block.append('    ("extract(", "Code Execution", "Medium", "extract() on untrusted input can overwrite variables unexpectedly and enable injection attacks.", "Avoid extract() on user-supplied data; access array keys explicitly."),\n')
insert_block.append("]\n")

lines[idx+1:idx+1] = insert_block

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("INSERTED SUCCESSFULLY")
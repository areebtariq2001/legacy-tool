import main

test_code = '''<?php
$conn = mysql_connect("host", "user", "pass");
$result = mysql_query("SELECT * FROM users");
if (ereg("^[0-9]+$", $input)) {
    echo "numeric";
}
$parts = split("/,/", $csv_line);
mysql_close($conn);
?>'''

result = main.migrate_php(test_code)
print("=== Changes (auto-applied) ===")
for c in result["changes"]:
    if not c.startswith("REVIEW NEEDED"):
        print(" AUTO:", c)
print()
print("=== Review Needed ===")
for c in result["changes"]:
    if c.startswith("REVIEW NEEDED"):
        print(" REVIEW:", c[:80])
print()
print("=== Migrated code (mysql_query should NOT be auto-changed) ===")
print(result["migrated_code"])
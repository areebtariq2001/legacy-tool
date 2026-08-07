import main

test_php = '''<?php
function run_cmd($c) {
    system("process " . $c);
}
?>'''

result = main.scan_sensitive_data(test_php)
print("Sensitive-data findings:", [f["issue"] for f in result["findings"]])

result_php_analyze = main.analyze_php(test_php)
print("analyze_php issues:", result_php_analyze.get("issues", []))
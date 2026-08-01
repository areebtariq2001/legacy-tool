import main

test_code = '''<?php
$x = $HTTP_GET_VARS['id'];
set_magic_quotes_runtime(0);
ini_set('safe_mode', '1');
$result = preg_replace('/pattern/e', 'code', $str);
?>'''

result = main.analyze_php(test_code)
print("Issues found:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)
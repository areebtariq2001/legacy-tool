import main

test_code = '''<?php
$DB_HOST = "10.0.4.12";
$DB_USER = "root";
$DB_PASS = "Bank@1234";
$DB_NAME = "core_banking";
$AML_API_KEY = "sk_live_9f3a2b7c1d8e";

function get_customer($customer_id) {
    $sql = "SELECT * FROM customers WHERE id = '" . $customer_id . "'";
    $res = mysql_query($sql);
    return mysql_fetch_array($res);
}
?>'''

result = main.analyze_php(test_code)
print("Total issues:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)
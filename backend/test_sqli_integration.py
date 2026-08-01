import main

test_code = '''<?php
function get_customer($customer_id) {
    $query = "SELECT * FROM customers WHERE id = '" . $customer_id . "'";
    return mysqli_query($conn, $query);
}
?>'''

result = main.analyze_php(test_code)
print("Issues found:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)
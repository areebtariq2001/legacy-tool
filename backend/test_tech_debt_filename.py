import main

test_code = '''<?php
function get_customer($id) {
    $sql = mysql_query("SELECT * FROM t");
    if (ereg("x", $id)) {
        return true;
    }
    return false;
}
?>'''

result_without = main.calculate_tech_debt(test_code)
result_with = main.calculate_tech_debt(test_code, "test.php")

print("WITHOUT filename - debt_score:", result_without["debt_score"], "- items:", len(result_without["items"]))
print("WITH filename - debt_score:", result_with["debt_score"], "- items:", len(result_with["items"]))
for item in result_with["items"]:
    print(" -", item["issue"])
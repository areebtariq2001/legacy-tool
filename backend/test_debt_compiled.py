import main

test_code = '''function old_style_array() {
    $arr = array("a" => 1, "b" => 2);
    return each($arr);
}'''

result = main.calculate_tech_debt(test_code, "test.php")
print("Result:", result)
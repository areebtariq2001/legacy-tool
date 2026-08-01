import main

test_code = '''<?php
class Account {
    var $id;
    function Account($id) {
        $this->id = $id;
    }
}
function calculate_premium($amount) {
    return money_format('%.2n', $amount);
}
?>'''

result = main.analyze_php(test_code)
print("Issues found:", len(result["issues"]))
for issue in result["issues"]:
    print(" -", issue)
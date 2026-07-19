import main
code = "<?php`nclass BankAccount {`n    function getBalance($id) {`n        return 100;`n    }`n    function updateBalance($id, $amount) {`n        return true;`n    }`n}"
r = main.generate_architecture(code, "Test.php")
print(r.get("arch_stats"))

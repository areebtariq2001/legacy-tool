import main

test_code = '''<?php
function process_wire_transfer($account, $amount, $swift_code) {
    $region = $swift_code{0};
    return $region;
}
?>'''

result = main.migrate_php(test_code)
print("Changes:", result["changes"])
print()
print("Migrated code contains {0}:", "$swift_code{0}" in result["migrated_code"])
print("Migrated code contains [0]:", "$swift_code[0]" in result["migrated_code"])
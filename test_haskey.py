import main
test_code = "if d.has_key(get_key(x)):\n    pass"
result = main.migrate_code(test_code)
with open("hk_test_result.txt", "w", encoding="utf-8") as out:
    out.write("MIGRATED CODE:\n" + result["migrated_code"] + "\n\nCHANGES:\n" + str(result["changes"]))
print("DONE genuinely")

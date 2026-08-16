import main
test_code = "# xrange removed in py3; raw_input renamed to input in py3\nfor i in xrange(3):\n    pass"
r = main.migrate_code(test_code)
with open("comment_corrupt_result.txt", "w", encoding="utf-8") as out:
    out.write("MIGRATED-CODE:\n" + r["migrated_code"])
print("COMMENT-CORRUPT-TEST-COMPLETED")
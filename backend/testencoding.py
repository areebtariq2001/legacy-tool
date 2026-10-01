import main

with open("testencoding_result.txt", "w", encoding="utf-8") as out:
    # Test 1: Latin-1 encoded content with non-UTF-8-valid bytes (e.g. a COBOL comment with accented characters)
    latin1_text = "* COBOL comment with café and naïve résumé\n01 WS-NAME PIC X(20)."
    latin1_bytes = latin1_text.encode("latin-1")
    result1, error1 = main.safe_read_file(latin1_bytes, "test.cbl")
    out.write("Test-1 (Latin-1-bytes-decode): error=" + str(error1) + chr(10))
    out.write("Genuinely-content-preserved-correctly: " + str(result1 == latin1_text if result1 else False) + " (expect True - no data loss)" + chr(10))
    out.write("Genuinely-result: " + repr(result1)[:150] + chr(10) + chr(10))

    # Test 2: UTF-8 encoded content WITH a BOM
    bom_text = "\ufeffdef hello():\n    print('world')"
    bom_bytes = bom_text.encode("utf-8")
    result2, error2 = main.safe_read_file(bom_bytes, "test.py")
    out.write("Test-2 (UTF-8-BOM-stripping): error=" + str(error2) + chr(10))
    out.write("Genuinely-BOM-stripped: " + str(not result2.startswith("\ufeff") if result2 else False) + " (expect True)" + chr(10))
    out.write("Genuinely-starts-with-def: " + str(result2.startswith("def") if result2 else False) + " (expect True)")
print("TESTENCODING-DONE")
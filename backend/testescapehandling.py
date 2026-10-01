import main

with open("testescapehandling_result.txt", "w", encoding="utf-8") as out:
    test_line = 'x = "Hello \\"World\\""  # genuine comment'
    out.write("Genuinely-test_line: " + repr(test_line) + chr(10) + chr(10))
    before, after = main._split_inline_comment(test_line)
    out.write("Genuinely-before (code-part): " + repr(before) + chr(10))
    out.write("Genuinely-after (comment-part): " + repr(after) + chr(10) + chr(10))
    out.write("Genuinely-correctly-preserved-full-string: " + str('Hello \\"World\\"' in before) + " (expect True)" + chr(10))
    out.write("Genuinely-comment-correctly-isolated: " + str(after == '# genuine comment') + " (expect True)")
print("TESTESCAPEHANDLING-DONE")
import main

with open("testheadanchor_result.txt", "w", encoding="utf-8") as out:
    # Test 1: normal operation still works
    bc = main.StarBuildBlockchain()
    for i in range(5):
        bc.add_block("action" + str(i), "f" + str(i) + ".py", "u@t.com", "1.1.1.1", "result" + str(i))
    valid1, reason1 = bc.verify_chain()
    out.write("Test-1 (normal-6-blocks-valid): valid=" + str(valid1) + " (expect True)\n\n")

    # Test 2: EXACT advisor scenario - 6 blocks total, delete last 3
    out.write("Genuinely-chain-length-before-delete: " + str(len(bc.chain)) + chr(10))
    del bc.chain[-3:]
    out.write("Genuinely-chain-length-after-delete: " + str(len(bc.chain)) + chr(10))
    valid2, reason2 = bc.verify_chain()
    out.write("Test-2 (advisor-scenario-delete-last-3-blocks): valid=" + str(valid2) + " reason=" + str(reason2) + chr(10))
    out.write("Genuinely-truncation-now-detected: " + str(valid2 == False) + " (expect True - this was the bug)\n\n")

    # Test 3: normal trim-to-2000 behavior should NOT false-positive
    bc2 = main.StarBuildBlockchain()
    bc2.add_block("a", "f.py", "u@t.com", "1.1.1.1", "r")
    bc2._next_index = 2000
    bc2.add_block("a2", "f2.py", "u@t.com", "1.1.1.1", "r2")  # this triggers del self.chain[:-2000] internally
    valid3, reason3 = bc2.verify_chain()
    out.write("Test-3 (normal-trim-operation-not-falsely-flagged): valid=" + str(valid3) + " (expect True)")
print("TESTHEADANCHOR-DONE")
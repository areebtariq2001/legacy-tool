import main

with open("testblockchainfinal_result.txt", "w", encoding="utf-8") as out:
    # Fresh blockchain instance
    bc = main.StarBuildBlockchain()

    # Test 1: normal operation still works
    b1 = bc.add_block("test-action", "test.py", "user@test.com", "1.2.3.4", "test-result")
    valid1, reason1 = bc.verify_chain()
    out.write("Test-1 (normal-add-and-verify): valid=" + str(valid1) + " (expect True)\n\n")

    # Test 2: simulate reaching the 2000-block threshold WITHOUT actually mining 2000 blocks (too slow)
    bc._next_index = 2000
    b2 = bc.add_block("test-action-2", "test2.py", "user@test.com", "1.2.3.4", "result-2")
    b3 = bc.add_block("test-action-3", "test3.py", "user@test.com", "1.2.3.4", "result-3")
    out.write("Test-2 (index-uniqueness-after-2000-threshold): b2.index=" + str(b2.index) + " b3.index=" + str(b3.index) + " (expect 2000 and 2001, NOT both 2000)\n")
    out.write("Genuinely-indices-unique: " + str(b2.index != b3.index) + " (expect True)\n\n")

    # Test 3: proof-of-work tampering detection
    bc2 = main.StarBuildBlockchain()
    bc2.add_block("a", "f.py", "u@t.com", "1.1.1.1", "r")
    bc2.chain[-1].hash = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"  # fake hash NOT starting with 00, but won't match compute_hash either
    valid3, reason3 = bc2.verify_chain()
    out.write("Test-3 (tampered-hash-not-matching-recompute): valid=" + str(valid3) + " (expect False)\n\n")

    # Test 4: genesis block tampering now detected
    bc3 = main.StarBuildBlockchain()
    bc3.chain[0].action = "TAMPERED-GENESIS"
    valid4, reason4 = bc3.verify_chain()
    out.write("Test-4 (tampered-genesis-block-detected): valid=" + str(valid4) + " reason=" + str(reason4) + " (expect False, reason=0)")
print("TESTBLOCKCHAINFINAL-DONE")
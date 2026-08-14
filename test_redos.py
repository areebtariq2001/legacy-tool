import time
import main
test_input = "x = " + chr(34) + ("a" * 20000) + chr(34)
start = time.time()
result = main.scan_sensitive_data(test_input)
elapsed = time.time() - start
with open("redos_test_result.txt", "w") as out:
    out.write("20000-char-input-genuinely-time: " + str(elapsed) + " seconds")
print("DONE genuinely - time:", elapsed)

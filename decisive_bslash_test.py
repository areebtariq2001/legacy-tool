import main
import inspect

src = inspect.getsource(main.check_regulatory_framework)
idx = src.find("car")
raw_snippet = src[idx-3:idx+10]
with open("bslash_test_output.txt", "w", encoding="utf-8") as out:
    out.write("Raw bytes around 'car': " + repr(raw_snippet) + "\n")
    import re
    test_pattern = None
    # Extract the actual pattern used in the function
    for line in src.split(chr(10)):
        if "Capital adequacy" in line:
            out.write("Full line: " + repr(line) + "\n")

print("DONE")
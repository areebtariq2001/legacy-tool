import main
import inspect

with open("recheck_smells_result.txt", "w", encoding="utf-8") as out:
    out.write(inspect.getsource(main.detect_code_smells))

print("RECHECK-COMPLETED")
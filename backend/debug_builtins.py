import main
print("print in _PY_BUILTINS:", "print" in main._PY_BUILTINS)
print("len in _PY_BUILTINS:", "len" in main._PY_BUILTINS)
print("Total builtins count:", len(main._PY_BUILTINS))
print("Type of __builtins__ in main module:", type(main.__builtins__))
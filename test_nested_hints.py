import main
test1 = "def f(x=g(1)):\n    pass"
r1 = main.funcs_has_no_hints(test1)
with open("nested_hint_test.txt", "w", encoding="utf-8") as out:
    out.write("def-f(x=g(1))-genuinely-no-hints-result: " + str(r1))
print("DONE genuinely")

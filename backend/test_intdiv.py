import main
code = "def calculate_interest(principal, rate, years):\n    simple_interest = (principal * rate * years) / 100\n    return simple_interest"
r = main.migrate_code(code)
print("---CHANGES---")
for c in r.get("changes"):
    print(c)
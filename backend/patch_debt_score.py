with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    debt_score = min(100, total_count * 8)
    try:
        _comp = calculate_complexity(source)
        if _comp["complexity_level"] in ["High complexity", "Very high complexity"] and debt_score < 20:
            debt_score = 25
        elif _comp["complexity_level"] == "Moderate complexity" and debt_score < 15:
            debt_score = 15
        if _comp["complexity_level"] in ["High complexity", "Very high complexity", "Moderate complexity"] and total_minutes < 60:
            total_minutes = max(total_minutes, 60)
    except Exception:
        pass'''

new = '''    ISSUE_WEIGHT_PER_MINUTE = 8
    MIN_SCORE_HIGH_COMPLEXITY = 25
    MIN_SCORE_MODERATE_COMPLEXITY = 15
    MIN_MINUTES_IF_COMPLEX = 60
    debt_score = min(100, total_count * ISSUE_WEIGHT_PER_MINUTE)
    try:
        _comp = calculate_complexity(source)
        if _comp["complexity_level"] in ["High complexity", "Very high complexity"] and debt_score < 20:
            debt_score = MIN_SCORE_HIGH_COMPLEXITY
        elif _comp["complexity_level"] == "Moderate complexity" and debt_score < 15:
            debt_score = MIN_SCORE_MODERATE_COMPLEXITY
        if _comp["complexity_level"] in ["High complexity", "Very high complexity", "Moderate complexity"] and total_minutes < 60:
            total_minutes = max(total_minutes, MIN_MINUTES_IF_COMPLEX)
    except Exception as e:
        print("Warning: complexity calculation failed in calculate_tech_debt: " + str(e))'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")
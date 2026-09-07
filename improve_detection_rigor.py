with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    _time_control_func_pattern = re.compile(r"(?i)(check.*hour|hour.*check|unusual.?hour|time.?of.?day|transaction.?time)")
    _file_has_dedicated_time_control = any(isinstance(n, ast.FunctionDef) and _time_control_func_pattern.search(n.name) for n in ast.walk(tree))'''
new1 = '''    _time_control_func_pattern = re.compile(r"(?i)(check.*hour|hour.*check|unusual.?hour|time.?of.?day|transaction.?time)")
    _comparison_op_pattern = re.compile(r"(>=|<=|>|<|==)\\s*\\d")
    _file_has_dedicated_time_control = any(isinstance(n, ast.FunctionDef) and _time_control_func_pattern.search(n.name) and _comparison_op_pattern.search(ast.get_source_segment(source, n) or "") for n in ast.walk(tree))'''
c1 = content.count(old1)
print("c1:", c1)
if c1 == 1:
    content = content.replace(old1, new1, 1)

old2 = '''    _geo_control_func_pattern = re.compile(r"(?i)(check.*geo|geo.*check|geo.?location|cross.?border|location.?check)")
    _file_has_dedicated_geo_control = any(isinstance(n, ast.FunctionDef) and _geo_control_func_pattern.search(n.name) for n in ast.walk(tree))'''
new2 = '''    _geo_control_func_pattern = re.compile(r"(?i)(check.*geo|geo.*check|geo.?location|cross.?border|location.?check)")
    _geo_body_signal_pattern = re.compile(r"(?i)(!=|==|not\\s+in|in\\s+\\[)")
    _file_has_dedicated_geo_control = any(isinstance(n, ast.FunctionDef) and _geo_control_func_pattern.search(n.name) and _geo_body_signal_pattern.search(ast.get_source_segment(source, n) or "") for n in ast.walk(tree))'''
c2 = content.count(old2)
print("c2:", c2)
if c2 == 1:
    content = content.replace(old2, new2, 1)

old3 = '''    _velocity_control_func_pattern = re.compile(r"(?i)(structur|smurf|velocity.?check)")
    _file_has_dedicated_velocity_control = any(isinstance(n, ast.FunctionDef) and _velocity_control_func_pattern.search(n.name) for n in ast.walk(tree))'''
new3 = '''    _velocity_control_func_pattern = re.compile(r"(?i)(structur|smurf|velocity.?check)")
    _velocity_body_signal_pattern = re.compile(r"(>=|<=|>|<|==|\\+=)")
    _file_has_dedicated_velocity_control = any(isinstance(n, ast.FunctionDef) and _velocity_control_func_pattern.search(n.name) and _velocity_body_signal_pattern.search(ast.get_source_segment(source, n) or "") for n in ast.walk(tree))'''
c3 = content.count(old3)
print("c3:", c3)
if c3 == 1:
    content = content.replace(old3, new3, 1)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("DETECTION-RIGOR-DONE")
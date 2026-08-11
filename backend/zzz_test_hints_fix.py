import main

test1 = '''
def a(x): pass
def b(x): pass
def with_hint(x: int): pass
'''
print("9-of-10-missing genuinely detects:", main.funcs_has_no_hints(test1))

test2 = '''def func(items, sep=":"): pass'''
print("Default-value-colon genuinely-NOT-false-positive:", main.funcs_has_no_hints(test2))

test3 = '''def a(x: int): pass
def b(y: str): pass'''
print("All-hinted genuinely-False:", main.funcs_has_no_hints(test3))
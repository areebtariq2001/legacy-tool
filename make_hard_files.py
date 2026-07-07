import os

os.makedirs("test_files", exist_ok=True)

hard_files = {
"empty_file.py": '''''',

"only_comments.py": '''# This file has only comments
# No actual code here
# Just testing edge case
''',

"mixed_py2_py3.py": '''# Mix of Python 2 and 3 style
print("Already python 3")
print "This is python 2"
for i in xrange(10):
    print(i)
''',

"weird_indent.py": '''def messy():
        x = 1
        if x == 1:
              print "deeply indented"
        return x
messy()
''',

"big_file.py": '''# A larger file with many functions
def func1():
    print "function 1"
def func2():
    for i in xrange(100):
        print i
def func3():
    d = {"a": 1}
    if d.has_key("a"):
        print d["a"]
def func4():
    name = raw_input("name: ")
    print "Hello", name
def func5():
    try:
        x = 1 / 0
    except ZeroDivisionError, e:
        print "Error:", e
def func6():
    nums = [1, 2, 3]
    result = map(lambda x: x * 2, nums)
    print result
def func7():
    for k, v in {"x": 1}.iteritems():
        print k, v
func1()
func2()
func3()
func4()
func5()
func6()
func7()
''',
}

for filename, content in hard_files.items():
    path = os.path.join("test_files", filename)
    with open(path, "w") as f:
        f.write(content)

print("Created", len(hard_files), "hard test files!")
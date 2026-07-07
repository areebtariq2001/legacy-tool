# A larger file with many functions
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

# Python 2 calculator
def divide(a, b):
    if b <> 0:
        return a / b
    else:
        print "Cannot divide by zero"
        return None

for i in xrange(5):
    print "Result:", divide(10, i)

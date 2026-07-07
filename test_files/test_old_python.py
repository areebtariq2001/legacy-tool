print "Hello World"
for i in xrange(10):
    print i
name = raw_input("Enter name: ")
d = {"a": 1}
if d.has_key("a"):
    print "found"
for k, v in d.iteritems():
    print k, v
try:
    x = 1
except Exception, e:
    print e
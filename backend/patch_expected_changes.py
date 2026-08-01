with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    expected_changes = {"xrange", "raw_input", "unicode", "basestring", "iteritems", "itervalues", "iterkeys", "has_key"}'''

new = '''    expected_changes = {"xrange", "raw_input", "unicode", "basestring", "iteritems", "itervalues", "iterkeys", "has_key", "urllib2", "cPickle", "StringIO", "cStringIO", "httplib", "xmlrpclib", "urlfetch", "cmp", "execfile", "reload", "unichr", "long"}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")
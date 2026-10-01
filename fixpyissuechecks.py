main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''py_issue_checks = [
        ('xrange', "xrange() found - use range()"),
        ('raw_input', "raw_input() found - use input()"),
        ('has_key', "dict.has_key() found - use 'in' operator"),
        ('iteritems', "iteritems() found - use items()"),
        ('itervalues', "itervalues() found - use values()"),
        ('iterkeys', "iterkeys() found - use keys()"),
        ('unicode(', "unicode() found - use str()"),
        ('basestring', "basestring found - use str"),
        ('urllib2', "urllib2 found - use urllib.request"),
        ('commands.getoutput', "commands module found - use subprocess"),
        ('itertools.izip', "izip found - use built-in zip()"),
        ('itertools.imap', "imap found - use built-in map()"),
        ('itertools.ifilter', "ifilter found - use built-in filter()"),
        ('.sort(cmp=', "sort(cmp=...) found - use key= instead"),
        ('<>', "<> operator found - use !="),
        ('apply(', "apply() found - use func(*args)"),
        ('execfile(', "execfile() found - use exec(open(...).read())"),
        ('reduce(', "reduce() found - import from functools"),
        ('StringIO', "StringIO found - use io.StringIO"),
        ('cPickle', "cPickle found - use pickle"),
        ('__cmp__', "__cmp__ found - use rich comparison methods"),
    ]
    for pattern, msg in py_issue_checks:
        if pattern in source:
            issues.append(msg)'''

new = '''py_issue_checks = [
        (r'\\bxrange\\b', "xrange() found - use range()"),
        (r'\\braw_input\\b', "raw_input() found - use input()"),
        (r'\\bhas_key\\b', "dict.has_key() found - use 'in' operator"),
        (r'\\biteritems\\b', "iteritems() found - use items()"),
        (r'\\bitervalues\\b', "itervalues() found - use values()"),
        (r'\\biterkeys\\b', "iterkeys() found - use keys()"),
        (r'\\bunicode\\(', "unicode() found - use str()"),
        (r'\\bbasestring\\b', "basestring found - use str"),
        (r'\\burllib2\\b', "urllib2 found - use urllib.request"),
        (r'\\bcommands\\.getoutput\\b', "commands module found - use subprocess"),
        (r'\\bitertools\\.izip\\b', "izip found - use built-in zip()"),
        (r'\\bitertools\\.imap\\b', "imap found - use built-in map()"),
        (r'\\bitertools\\.ifilter\\b', "ifilter found - use built-in filter()"),
        (r'\\.sort\\(cmp=', "sort(cmp=...) found - use key= instead"),
        (r'<>', "<> operator found - use !="),
        (r'\\bapply\\(', "apply() found - use func(*args)"),
        (r'\\bexecfile\\(', "execfile() found - use exec(open(...).read())"),
        (r'\\breduce\\(', "reduce() found - import from functools"),
        (r'\\bStringIO\\b', "StringIO found - use io.StringIO"),
        (r'\\bcPickle\\b', "cPickle found - use pickle"),
        (r'__cmp__', "__cmp__ found - use rich comparison methods"),
    ]
    for pattern, msg in py_issue_checks:
        if re.search(pattern, source):
            issues.append(msg)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXPYISSUECHECKS-DONE")
else:
    print("FAILED - count was:", count)
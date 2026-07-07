# string processing
def process(text):
    if isinstance(text, basestring):
        return unicode(text).upper()
    return text

names = ["ali", "sara"]
result = map(lambda x: process(x), names)
print result

def read_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

try:
    data = read_lines("test.txt")
    print "Read", len(data), "lines"
except IOError, e:
    print "Error:", e

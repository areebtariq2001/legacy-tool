def find(items, target):
    for i in xrange(len(items)):
        if items[i] == target:
            return i
    return -1

data = [5, 3, 8, 1]
pos = find(data, 8)
print "Found at:", pos

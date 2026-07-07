counts = {}
words = ["a", "b", "a", "c", "a"]
for w in words:
    if counts.has_key(w):
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

for word, count in counts.iteritems():
    print word, "appears", count, "times"

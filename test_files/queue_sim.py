class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def size(self):
        return len(self.items)

q = Queue()
for i in xrange(5):
    q.enqueue(i)
print "Queue size:", q.size()

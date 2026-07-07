# Python 2 shopping cart
class Cart:
    def __init__(self):
        self.items = {}
    def add(self, name, price):
        if self.items.has_key(name):
            print "Already in cart"
        else:
            self.items[name] = price
    def total(self):
        t = 0
        for k, v in self.items.iteritems():
            t = t + v
        return t

cart = Cart()
cart.add("book", 10)
name = raw_input("Item: ")
print "Total:", cart.total()

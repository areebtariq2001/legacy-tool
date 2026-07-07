import os

os.makedirs("test_files", exist_ok=True)

files = {
"shopping_cart.py": '''# Python 2 shopping cart
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
''',

"calculator.py": '''# Python 2 calculator
def divide(a, b):
    if b <> 0:
        return a / b
    else:
        print "Cannot divide by zero"
        return None

for i in xrange(5):
    print "Result:", divide(10, i)
''',

"user_data.py": '''import urllib2
import cPickle

def fetch(url):
    response = urllib2.urlopen(url)
    return response.read()

def save(data, f):
    cPickle.dump(data, open(f, "w"))

users = {"a": 1, "b": 2}
for k in users.iterkeys():
    print k
''',

"string_utils.py": '''# string processing
def process(text):
    if isinstance(text, basestring):
        return unicode(text).upper()
    return text

names = ["ali", "sara"]
result = map(lambda x: process(x), names)
print result
''',

"file_reader.py": '''def read_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

try:
    data = read_lines("test.txt")
    print "Read", len(data), "lines"
except IOError, e:
    print "Error:", e
''',

"counter.py": '''counts = {}
words = ["a", "b", "a", "c", "a"]
for w in words:
    if counts.has_key(w):
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

for word, count in counts.iteritems():
    print word, "appears", count, "times"
''',

"temperature.py": '''def convert():
    celsius = input("Enter celsius: ")
    fahrenheit = celsius * 9 / 5 + 32
    print "Fahrenheit:", fahrenheit

convert()
''',

"bank.py": '''class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            print "Insufficient funds"
        else:
            self.balance = self.balance - amount
            print "New balance:", self.balance

acc = Account(100)
acc.withdraw(30)
''',

"grades.py": '''students = {"ali": 85, "sara": 92, "ahmed": 78}
total = 0
for name, grade in students.iteritems():
    total = total + grade
    print name, ":", grade
print "Average:", total / len(students)
''',

"loop_test.py": '''result = []
for i in xrange(100):
    if i % 2 == 0:
        result.append(i)
print "Even numbers:", result
print "Count:", len(result)
''',

"menu.py": '''def show_menu():
    print "1. Start"
    print "2. Exit"
    choice = raw_input("Choose: ")
    return choice

c = show_menu()
print "You chose:", c
''',

"inventory.py": '''inventory = {"apple": 50, "banana": 30}
def check(item):
    if inventory.has_key(item):
        print item, "in stock:", inventory[item]
    else:
        print item, "not found"

check("apple")
check("orange")
''',

"math_ops.py": '''import math
def stats(numbers):
    total = reduce(lambda a, b: a + b, numbers)
    avg = total / len(numbers)
    return avg

nums = [10, 20, 30, 40]
print "Average:", stats(nums)
''',

"logger.py": '''import sys
def log(message):
    print >> sys.stderr, "LOG:", message

log("Application started")
log("Processing data")
''',

"queue_sim.py": '''class Queue:
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
''',

"config.py": '''settings = {"debug": True, "port": 8080}
for key, value in settings.iteritems():
    print "%s = %s" % (key, value)
''',

"validator.py": '''def validate_age(age):
    age = int(raw_input("Enter age: "))
    if age < 0:
        print "Invalid"
    elif age <> age:
        print "Strange"
    else:
        print "Valid age:", age
''',

"matrix.py": '''def make_matrix(rows, cols):
    matrix = []
    for i in xrange(rows):
        row = []
        for j in xrange(cols):
            row.append(i * j)
        matrix.append(row)
    return matrix

m = make_matrix(3, 3)
print m
''',

"search.py": '''def find(items, target):
    for i in xrange(len(items)):
        if items[i] == target:
            return i
    return -1

data = [5, 3, 8, 1]
pos = find(data, 8)
print "Found at:", pos
''',

"broken_file.py": '''# This file has a deliberate problem
def calculate(x)
    result = x * 2
    print result
calculate(5)
''',
}

for filename, content in files.items():
    path = os.path.join("test_files", filename)
    with open(path, "w") as f:
        f.write(content)

print("Created", len(files), "test files in test_files folder!")
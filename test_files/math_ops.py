import math
def stats(numbers):
    total = reduce(lambda a, b: a + b, numbers)
    avg = total / len(numbers)
    return avg

nums = [10, 20, 30, 40]
print "Average:", stats(nums)

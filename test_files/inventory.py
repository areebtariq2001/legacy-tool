inventory = {"apple": 50, "banana": 30}
def check(item):
    if inventory.has_key(item):
        print item, "in stock:", inventory[item]
    else:
        print item, "not found"

check("apple")
check("orange")

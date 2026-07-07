def show_menu():
    print "1. Start"
    print "2. Exit"
    choice = raw_input("Choose: ")
    return choice

c = show_menu()
print "You chose:", c

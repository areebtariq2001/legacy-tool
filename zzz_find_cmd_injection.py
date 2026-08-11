import main

for name in dir(main):
    if 'command' in name.lower() and 'inject' in name.lower():
        print(name)
    if 'scan_sensitive' in name.lower():
        print(name)
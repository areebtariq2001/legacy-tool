with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old4 = '''        except:
            pass
        entries.append(entry)'''
new4 = '''        except Exception as e:
            entry["parse_error"] = str(e)
        entries.append(entry)'''

old6 = '''    (r"\\b(?:\\d[ -]*?){13,16}\\b", "Possible card number", "High"),'''
new6 = '''    (r"\\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\\b", "Possible credit card number (Visa/Mastercard/Amex/Discover pattern)", "High"),'''

count4 = content.count(old4)
count6 = content.count(old6)
print("Bug-4 occurrences:", count4)
print("Bug-6 occurrences:", count6)

if count4 == 1:
    content = content.replace(old4, new4, 1)
    print("Bug-4 PATCHED")
if count6 == 1:
    content = content.replace(old6, new6, 1)
    print("Bug-6 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")
import main
import hashlib

out = open("testpbkdf2b_result.txt", "w", encoding="utf-8")

old_salt = "abc123"
old_password = "MyOldPassword123"
old_style_hash_value = hashlib.pbkdf2_hmac("sha256", old_password.encode("utf-8"), old_salt.encode("utf-8"), 200000).hex()
old_format_stored_hash = old_salt + "$" + old_style_hash_value

result1 = main._verify_password(old_password, old_format_stored_hash)
out.write("Test1-old-format-correct-password: " + str(result1) + " expect True\n")

result2 = main._verify_password("WrongPassword", old_format_stored_hash)
out.write("Test2-old-format-wrong-password: " + str(result2) + " expect False\n")

new_password = "MyNewPassword456"
new_format_stored_hash = main._hash_password(new_password)
out.write("New-hash-parts-count: " + str(len(new_format_stored_hash.split("$"))) + " expect 3\n")

result3 = main._verify_password(new_password, new_format_stored_hash)
out.write("Test3-new-format-correct-password: " + str(result3) + " expect True\n")

result4 = main._verify_password("WrongPassword", new_format_stored_hash)
out.write("Test4-new-format-wrong-password: " + str(result4) + " expect False\n")

out.close()
print("TESTPBKDF2B-DONE")
import main
import hashlib

with open("testpbkdf2_result.txt", "w", encoding="utf-8") as out:
    # Simulate an OLD-FORMAT hash (as it would have been stored BEFORE this fix, with 200k iterations, 2-part format)
    old_salt = "abc123"
    old_password = "MyOldPassword123"
    old_style_hash_value = hashlib.pbkdf2_hmac("sha256", old_password.encode("utf-8"), old_salt.encode("utf-8"), 200000).hex()
    old_format_stored_hash = old_salt + "$" + old_style_hash_value

    result1 = main._verify_password(old_password, old_format_stored_hash)
    out.write("Test-1 (existing-user-with-OLD-2-part-200k-hash, correct-password): " + str(result1) + " (expect True - existing users must not be locked out)" + chr(10))

    result2 = main._verify_password("WrongPassword", old_format_stored_hash)
    out.write("Test-2 (OLD-format-hash, wrong-password): " + str(result2) + " (expect False)" + chr(10) + chr(10))

    # New user: hash created with the new function should use 600k and verify correctly
    new_password = "MyNewPassword456"
    new_format_stored_hash = main._hash_password(new_password)
    out.write("Genuinely-new-hash-format: " + new_format_stored_hash[:60] + "..." + chr(10))
    out.write("Genuinely-new-hash-has-3-parts (salt$iterations$hash): " + str(len(new_format_stored_hash.split("$")) == 3) + chr(10))

    result3 = main._verify_password(new_password, new_format_stored_hash)
    out.write("Test-3 (new-user-with-NEW-3-part-600k-hash, correct-password): " + str(result3) + " (expect True)" + chr(10))

    result4 = main._verify_password("WrongPassword", new_format_stored_hash)
    out.write("Test-4 (NEW-format-hash, wrong-password): " + str(result4) + "
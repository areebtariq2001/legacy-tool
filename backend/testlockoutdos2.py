import main
import time

victim_email = "dos-test-victim2@test.com"
attacker_ip = "6.6.6.6"
victim_ip = "7.7.7.7"

# Directly simulate 5 already-recorded failed attempts for (victim_email, attacker_ip)
attacker_key = victim_email + "|" + attacker_ip
now = time.time()
main._failed_login_attempts[attacker_key] = [now - 100, now - 80, now - 60, now - 40, now - 20]

# Attacker's 6th attempt from the same IP should now be hard-blocked
result_attacker = main.login_user(victim_email, "wrongpassword", ip=attacker_ip)

# Victim, same email, DIFFERENT IP, with a clean (empty) attempt history should NOT be blocked
result_victim = main.login_user(victim_email, "wrongpassword", ip=victim_ip)

with open("testlockoutdos2_result.txt", "w", encoding="utf-8") as out:
    out.write("Test-1 (attacker, 5 prior attempts, same IP): " + str(result_attacker.get("error", "")) + chr(10))
    out.write("Genuinely-attacker-hard-blocked: " + str("Too many failed" in result_attacker.get("error", "")) + " (expect True)" + chr(10) + chr(10))
    out.write("Test-2 (victim, same email, DIFFERENT IP, no prior attempts): " + str(result_victim.get("error", "")) + chr(10))
    out.write("Genuinely-victim-NOT-hard-blocked: " + str("Too many failed" not in result_victim.get("error", "")) + " (expect True - proves email+ip isolation works)")
print("TESTLOCKOUTDOS2-DONE")
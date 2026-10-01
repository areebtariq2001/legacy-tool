import main

victim_email = "dos-test-victim@test.com"
attacker_ip = "6.6.6.6"
victim_ip = "7.7.7.7"

# Attacker sends 5 failed attempts against the victim's email from their own IP
for i in range(5):
    main.login_user(victim_email, "wrongpassword", ip=attacker_ip)

# 6th attempt from the SAME attacker IP should be locked out
result_attacker_6th = main.login_user(victim_email, "wrongpassword", ip=attacker_ip)

# The VICTIM, using the SAME email but from a DIFFERENT IP, should NOT be locked out
result_victim_own_ip = main.login_user(victim_email, "wrongpassword", ip=victim_ip)

with open("testlockoutdos_result.txt", "w", encoding="utf-8") as out:
    out.write("Test-1 (attacker-6th-attempt-same-IP): " + str(result_attacker_6th.get("error", "")) + chr(10))
    out.write("Genuinely-attacker-locked-out: " + str("Too many failed" in result_attacker_6th.get("error", "")) + " (expect True)" + chr(10) + chr(10))
    out.write("Test-2 (victim-different-IP-same-email): " + str(result_victim_own_ip.get("error", "")) + chr(10))
    out.write("Genuinely-victim-NOT-locked-out (should NOT say Too many failed): " + str("Too many failed" not in result_victim_own_ip.get("error", "")) + " (expect True - victim can still attempt from their own IP)")
print("TESTLOCKOUTDOS-DONE")
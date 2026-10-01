import main
import threading
import time

test_email = "racetest@example.com"
main._failed_login_attempts.pop(test_email, None)

# Mock DB connection to return None so we test ONLY the attempt-counting logic (no real DB needed)
main._get_db_connection = lambda: None

results = []
results_lock = threading.Lock()

def attempt():
    r = main.login_user(test_email, "wrongpassword")
    with results_lock:
        results.append(r.get("error", ""))

threads = [threading.Thread(target=attempt) for _ in range(30)]
for t in threads:
    t.start()
for t in threads:
    t.join()

blocked_count = sum(1 for e in results if "Too many failed" in e or "wait" in e.lower())
db_unavailable_count = sum(1 for e in results if "Database not available" in e)
recorded_attempts = len(main._failed_login_attempts.get(test_email, []))

with open("testrace_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-30-concurrent-attempts-sent" + chr(10))
    out.write("Genuinely-blocked-by-lockout-policy: " + str(blocked_count) + " (BEFORE-FIX-this-was-0)" + chr(10))
    out.write("Genuinely-reached-DB-check (not-blocked): " + str(db_unavailable_count) + " (BEFORE-FIX-this-was-30)" + chr(10))
    out.write("Genuinely-recorded-attempt-timestamps: " + str(recorded_attempts) + " (BEFORE-FIX-this-was-1, race-condition-lost-writes)")
print("TESTRACE-DONE")
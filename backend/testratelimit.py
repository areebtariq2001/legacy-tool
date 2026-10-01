import main
import threading

test_ip = "1.2.3.4-ratelimit-test"
main._rate_limit_store.pop(test_ip, None)

results = []
results_lock = threading.Lock()

def attempt():
    r = main._check_rate_limit(test_ip, max_requests=10, window_seconds=60)
    with results_lock:
        results.append(r)

threads = [threading.Thread(target=attempt) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()

allowed_count = sum(1 for r in results if r is True)
blocked_count = sum(1 for r in results if r is False)
recorded_count = len(main._rate_limit_store.get(test_ip, []))

with open("testratelimit_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-100-concurrent-requests-sent-with-max_requests=10" + chr(10))
    out.write("Genuinely-allowed (should be close to 10, NOT 100): " + str(allowed_count) + chr(10))
    out.write("Genuinely-blocked (should be close to 90): " + str(blocked_count) + chr(10))
    out.write("Genuinely-recorded-timestamps-in-store (should be close to 10, NOT 1 or 100): " + str(recorded_count))
print("TESTRATELIMIT-DONE")
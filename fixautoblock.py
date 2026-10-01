main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '_AUTO_BLOCK_EVENT_TYPES = {"honeypot_triggered", "scanner_signature_detected", "jailbreak_output_indicator"}'
new = '_AUTO_BLOCK_EVENT_TYPES = set()  # TEMPORARILY DISABLED: _get_client_ip may return the same address for all users behind Render\'s proxy if --proxy-headers is not yet configured on the Start Command - until verified, auto-blocking on 3 suspicious events could lock out every legitimate user at once from a single bad actor\'s 3 requests. Re-enable with the original 3 event types once IP detection is confirmed to distinguish real clients (test from 2 different devices/networks and compare logged IPs).'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXAUTOBLOCK-DONE")
else:
    print("FAILED - count was:", count)
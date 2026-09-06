with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '_txn_name_pattern = re.compile(r"(?i)(transfer|withdraw|deposit|payment|transaction|disburs)")'
c1 = content.count(old1)
print("Occurrences of unusual-hours-style pattern:", c1)

old2 = 'def check_unusual_hours_flag(source, filename):'
idx2 = content.find(old2)
print("check_unusual_hours_flag found at index:", idx2)

old3 = 'def check_geo_anomaly_detection(source, filename):'
idx3 = content.find(old3)
print("check_geo_anomaly_detection found at index:", idx3)

print("SCOPE-INVESTIGATION-DONE")
with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

marker1 = "def analyze_regulation_impact(source, filename):"
marker2 = "def calculate_change_risk_radar(source, filename):"
marker3 = "def detect_legacy_ghosts(source, filename):"
marker4 = "def detect_service_boundaries(source, filename):"

with open("fresh_count_result.txt", "w", encoding="utf-8") as out:
    out.write("analyze_regulation_impact count: " + str(content.count(marker1)) + chr(10))
    out.write("calculate_change_risk_radar count: " + str(content.count(marker2)) + chr(10))
    out.write("detect_legacy_ghosts count: " + str(content.count(marker3)) + chr(10))
    out.write("detect_service_boundaries count: " + str(content.count(marker4)) + chr(10))
    out.write("Total file size: " + str(len(content)) + " chars" + chr(10))
print("FRESH-COUNT-COMPLETED")
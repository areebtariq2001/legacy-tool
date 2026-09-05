import re as re_module

with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Find and replace old check_cnic_validation_quality function entirely
cnic_start = content.find("def check_cnic_validation_quality(source, filename):")
cnic_end = content.find("\n\n@app.post(\"/cnic-validation-check\")")
print("CNIC-start-found:", cnic_start != -1, "CNIC-end-found:", cnic_end != -1)

ntn_start = content.find("def check_ntn_strn_validation_quality(source, filename):")
ntn_end = content.find("\n\n@app.post(\"/ntn-strn-check\")")
print("NTN-start-found:", ntn_start != -1, "NTN-end-found:", ntn_end != -1)

with open("cnic_p1_out.txt", "r", encoding="utf-8") as f:
    new_cnic = f.read()
with open("ntn_p1_out.txt", "r", encoding="utf-8") as f:
    new_ntn = f.read()

if cnic_start != -1 and cnic_end != -1 and ntn_start != -1 and ntn_end != -1:
    content = content[:cnic_start] + new_cnic.rstrip() + content[cnic_end:ntn_start] + new_ntn.rstrip() + content[ntn_end:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("REPLACE-SUCCESSFUL")
else:
    print("REPLACE-FAILED - anchors not found")
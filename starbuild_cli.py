#!/usr/bin/env python3
"""
StarBuild CLI - Batch legacy code analysis from the command line.
Usage:
    python starbuild_cli.py <folder> [--mode analyze|migrate|risk|debt]
"""
import sys
import os
import json
import urllib.request
import urllib.error

API = "https://legacy-migration-tool-1.onrender.com"

ENDPOINTS = {
    "analyze": "/analyze",
    "migrate": "/migrate",
    "risk": "/risk-assessment",
    "debt": "/tech-debt",
    "scan": "/scan-sensitive",
    "banking": "/banking-patterns",
}

def send_file(filepath, endpoint):
    with open(filepath, "rb") as f:
        file_data = f.read()
    boundary = "----StarBuildBoundary"
    filename = os.path.basename(filepath)
    body = b""
    body += ("--" + boundary + "\r\n").encode()
    body += ('Content-Disposition: form-data; name="file"; filename="' + filename + '"\r\n').encode()
    body += b"Content-Type: application/octet-stream\r\n\r\n"
    body += file_data
    body += ("\r\n--" + boundary + "--\r\n").encode()
    req = urllib.request.Request(API + endpoint, data=body)
    req.add_header("Content-Type", "multipart/form-data; boundary=" + boundary)
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        return {"error": str(e)}

def print_result(filename, mode, result):
    print("\n" + "=" * 50)
    print("FILE: " + filename + "  |  MODE: " + mode)
    print("=" * 50)
    if "error" in result:
        print("  Error: " + str(result["error"]))
        return
    if mode == "analyze":
        print("  Functions: " + str(len(result.get("functions", []))))
        print("  Classes:   " + str(len(result.get("classes", []))))
        print("  Issues:    " + str(len(result.get("issues", []))))
        for issue in result.get("issues", [])[:10]:
            print("    - " + issue)
    elif mode == "migrate":
        changes = result.get("changes", [])
        print("  Changes applied: " + str(len(changes)))
        for c in changes:
            print("    - " + c)
    elif mode == "risk":
        print("  Overall: " + result.get("overall_risk", "N/A"))
        print("  High: %s  Medium: %s  Low: %s" % (result.get("high_count", 0), result.get("medium_count", 0), result.get("low_count", 0)))
        for fd in result.get("findings", []):
            print("    [%s] %s - %s" % (fd.get("risk_level"), fd.get("dependency"), fd.get("recommendation")))
    elif mode == "debt":
        print("  Debt Score: %s/100 (%s)" % (result.get("debt_score", 0), result.get("debt_level", "")))
        print("  Estimated effort: ~%s hours" % result.get("estimated_hours", 0))
    elif mode == "scan":
        print("  " + result.get("verdict", ""))
        print("  High: %s  Medium: %s  Low: %s" % (result.get("high_count", 0), result.get("medium_count", 0), result.get("low_count", 0)))
        for fd in result.get("findings", []):
            print("    [%s] %s (%sx)" % (fd.get("severity"), fd.get("issue"), fd.get("occurrences")))
    elif mode == "banking":
        print("  " + result.get("verdict", ""))
        for fd in result.get("findings", []):
            print("    - %s (%sx)" % (fd.get("pattern"), fd.get("occurrences")))

def main():
    if len(sys.argv) < 2:
        print("StarBuild CLI - Batch legacy code analysis")
        print("Usage: python starbuild_cli.py <folder> [--mode analyze|migrate|risk|debt|scan|banking]")
        print("Example: python starbuild_cli.py ./my_code --mode risk")
        return
    folder = sys.argv[1]
    mode = "analyze"
    if "--mode" in sys.argv:
        idx = sys.argv.index("--mode")
        if idx + 1 < len(sys.argv):
            mode = sys.argv[idx + 1]
    if mode not in ENDPOINTS:
        print("Unknown mode: " + mode + ". Valid: " + ", ".join(ENDPOINTS.keys()))
        return
    if not os.path.isdir(folder):
        print("Folder not found: " + folder)
        return
    py_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".py")]
    if not py_files:
        print("No .py files found in " + folder)
        return
    print("StarBuild CLI - processing %d file(s) in '%s' with mode '%s'" % (len(py_files), folder, mode))
    print("Contacting API (first request may take ~50s if server is asleep)...")
    endpoint = ENDPOINTS[mode]
    for fp in py_files:
        result = send_file(fp, endpoint)
        print_result(os.path.basename(fp), mode, result)
    print("\n" + "=" * 50)
    print("Done. Processed %d file(s)." % len(py_files))

if __name__ == "__main__":
    main()
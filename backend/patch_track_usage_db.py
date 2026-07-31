with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = 69
end_idx = 91

print("Line at start (70):", repr(lines[69]))
print("Line at end (91):", repr(lines[90]))

new_block = []
new_block.append("def write_audit_log(action, filename, result_summary):\n")
new_block.append("    try:\n")
new_block.append('        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")\n')
new_block.append("        conn = _get_db_connection()\n")
new_block.append("        if conn:\n")
new_block.append("            try:\n")
new_block.append("                cur = conn.cursor()\n")
new_block.append('                cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, result_summary))\n')
new_block.append("                conn.commit()\n")
new_block.append("                cur.close()\n")
new_block.append("                conn.close()\n")
new_block.append("                return\n")
new_block.append("            except Exception:\n")
new_block.append("                pass\n")
new_block.append("        with _stats_lock:\n")
new_block.append('            _in_memory_audit_log.insert(0, f"[{timestamp}] action={action} | file={filename} | result={result_summary}")\n')
new_block.append("            del _in_memory_audit_log[50:]\n")
new_block.append("    except Exception:\n")
new_block.append("        pass\n")
new_block.append("\n")
new_block.append("def track_usage(action, filename):\n")
new_block.append("    conn = _get_db_connection()\n")
new_block.append("    if conn:\n")
new_block.append("        try:\n")
new_block.append("            cur = conn.cursor()\n")
new_block.append('            cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, "tracked"))\n')
new_block.append("            conn.commit()\n")
new_block.append("            cur.close()\n")
new_block.append("            conn.close()\n")
new_block.append("        except Exception:\n")
new_block.append("            pass\n")
new_block.append("    with _stats_lock:\n")
new_block.append('        _in_memory_stats["total_files"] += 1\n')
new_block.append('        if "migrate" in action:\n')
new_block.append('            _in_memory_stats["total_migrations"] += 1\n')
new_block.append('        elif "analyze" in action:\n')
new_block.append('            _in_memory_stats["total_analyses"] += 1\n')
new_block.append('        _in_memory_stats["logs"].insert(0, {\n')
new_block.append('            "action": action,\n')
new_block.append('            "filename": filename,\n')
new_block.append('            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")\n')
new_block.append("        })\n")
new_block.append('        del _in_memory_stats["logs"][50:]\n')
new_block.append("\n")

lines[start_idx:end_idx] = new_block

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("PATCHED SUCCESSFULLY")
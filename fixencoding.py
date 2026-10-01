main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    try:
        source = content_bytes.decode("utf-8", errors="ignore")
    except Exception as e:
        return None, f"Could not read file (encoding issue): {str(e)}"'''

new = '''    try:
        source = content_bytes.decode("utf-8")
    except UnicodeDecodeError:
        # Not valid UTF-8 - likely a legacy-encoded file (e.g. Latin-1/CP1252 COBOL
        # source, common on older mainframe systems). Latin-1 can decode any byte
        # sequence without loss (unlike errors="ignore", which silently deletes
        # invalid bytes and can corrupt string literals, comments, or code).
        try:
            source = content_bytes.decode("latin-1")
        except Exception as e:
            return None, f"Could not read file (encoding issue): {str(e)}"
    except Exception as e:
        return None, f"Could not read file (encoding issue): {str(e)}"
    if source.startswith("\\ufeff"):
        source = source[1:]  # strip a leading UTF-8 byte-order-mark, which otherwise
        # shows up as a stray character before the first real line of code and can
        # confuse language/syntax detection that expects the file to start cleanly'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXENCODING-DONE")
else:
    print("FAILED - count was:", count)
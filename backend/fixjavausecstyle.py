main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Update migrate_java's main rules loop to use the C-style comment splitter
idx_start = content.find("def migrate_java")
idx_end = content.find("\ndef ", idx_start + 20)
java_body = content[idx_start:idx_end]

old1 = "_code_part, _comment_part = _split_inline_comment(_mline)"
new1 = "_code_part, _comment_part = _split_inline_comment_cstyle(_mline)"
results["1_main_loop_count_in_java"] = java_body.count(old1)
new_java_body = java_body.replace(old1, new1)

# Update the review_rules comment-stripping fix to use the C-style splitter too
old2 = "chr(10).join(_split_inline_comment(_l)[0] for _l in _migrated_no_comments.split(chr(10)))"
new2 = "chr(10).join(_split_inline_comment_cstyle(_l)[0] for _l in _migrated_no_comments.split(chr(10)))"
results["2_review_rules_count_in_java"] = new_java_body.count(old2)
new_java_body = new_java_body.replace(old2, new2)

content = content[:idx_start] + new_java_body + content[idx_end:]

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXJAVAUSECSTYLE-DONE")
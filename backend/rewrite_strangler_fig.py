with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

anchor = "def generate_strangler_fig_wrapper(source, filename):"
end_marker = "\ndef "
start_idx = content.find(anchor)
print("Anchor-found-at:", start_idx)

if start_idx != -1:
    search_from = start_idx + len(anchor)
    end_idx = content.find(end_marker, search_from)
    print("End-found-at:", end_idx)

    new_function = '''def generate_strangler_fig_wrapper(source, filename):
    import keyword as _kw
    if filename.lower().endswith(".py"):
        funcs = re.findall(r"^def\\s+(\\w+)\\s*\\(", source, re.MULTILINE)
    elif filename.lower().endswith(".java"):
        funcs = re.findall(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:synchronized\\s+)?[\\w<>\\[\\]]+\\s+(\\w+)\\s*\\([^)]*\\)\\s*(?:throws\\s+[\\w,\\s]+)?\\s*\\{", source)
    elif filename.lower().endswith(".php"):
        funcs = re.findall(r"function\\s+(\\w+)\\s*\\(", source)
    elif filename.lower().endswith((".cbl", ".cob")):
        funcs_raw = re.findall(r"(?mi)^(?:\\d{6}\\s+)?(?!END-)([\\w-]+)\\.\\s*$", source)
        _cobol_reserved_structural = {"IDENTIFICATION", "ENVIRONMENT", "DATA", "PROCEDURE", "DIVISION", "CONFIGURATION", "INPUT-OUTPUT", "FILE", "WORKING-STORAGE", "LINKAGE", "SECTION", "STOP", "EXIT", "RUN", "GOBACK"}
        funcs = [f for f in funcs_raw if f.upper() not in _cobol_reserved_structural]
    else:
        funcs = []
    funcs_full = list(dict.fromkeys(funcs))
    funcs_truncated = len(funcs_full) > 15
    funcs = funcs_full[:15]
    class_name = filename.rsplit(".", 1)[0].replace("-", "_").replace(" ", "_").replace(".", "_")
    if not class_name or not class_name[0].isalpha():
        class_name = "Legacy" + class_name
    wrapper_lines = []
    if filename.lower().endswith(".py"):
        wrapper_lines.append(f"# from {filename.rsplit('.', 1)[0]} import {', '.join(funcs)}  # <- adjust import path for your project")
        wrapper_lines.append(f"class {class_name}Facade:")
        wrapper_lines.append("    \\"\\"\\"Strangler Fig facade - routes calls to legacy or new implementation.\\"\\"\\"")
        wrapper_lines.append("    def __init__(self, use_new_impl=False):")
        wrapper_lines.append("        self.use_new_impl = use_new_impl")
        for fn in funcs:
            safe_fn = fn.replace("-", "_")
            if _kw.iskeyword(safe_fn):
                safe_fn = safe_fn + "_func"
            wrapper_lines.append("")
            wrapper_lines.append(f"    def {safe_fn}(self, *args, **kwargs):")
            wrapper_lines.append("        if self.use_new_impl:")
            wrapper_lines.append(f"            # TODO: call new implementation of {fn}")
            wrapper_lines.append("            raise NotImplementedError(\\"New implementation not yet wired up\\")")
            wrapper_lines.append(f"        return {fn}(*args, **kwargs)  # delegates to legacy function")
    elif filename.lower().endswith(".java"):
        wrapper_lines.append(f"public class {class_name}Facade {{")
        wrapper_lines.append("    private boolean useNewImpl = false;")
        wrapper_lines.append(f"    private {class_name} legacy = new {class_name}(); // TODO: adjust to your legacy class name/constructor")
        for fn in funcs:
            wrapper_lines.append("")
            wrapper_lines.append(f"    // TODO: replace Object with the actual return type and parameter types")
            wrapper_lines.append(f"    public Object {fn}(Object... args) {{")
            wrapper_lines.append("        if (useNewImpl) {")
            wrapper_lines.append(f"            // TODO: call new implementation of {fn}")
            wrapper_lines.append("            throw new UnsupportedOperationException(\\"New implementation not yet wired up\\");")
            wrapper_lines.append("        }")
            wrapper_lines.append(f"        return legacy.{fn}(args); // delegates to legacy instance - adjust signature/casting as needed")
            wrapper_lines.append("    }")
        wrapper_lines.append("}")
    elif filename.lower().endswith(".php"):
        wrapper_lines.append(f"class {class_name}Facade {{")
        wrapper_lines.append("    private $useNewImpl = false;")
        wrapper_lines.append("")
        wrapper_lines.append("    function __construct($useNewImpl = false) {")
        wrapper_lines.append("        $this->useNewImpl = $useNewImpl;")
        wrapper_lines.append("    }")
        for fn in funcs:
            wrapper_lines.append("")
            wrapper_lines.append(f"    function {fn}(...$args) {{")
            wrapper_lines.append("        if ($this->useNewImpl) {")
            wrapper_lines.append(f"            // TODO: call new implementation of {fn}")
            wrapper_lines.append("            throw new Exception(\\"New implementation not yet wired up\\");")
            wrapper_lines.append("        }")
            wrapper_lines.append(f"        return {fn}(...$args); // delegates to legacy")
            wrapper_lines.append("    }")
        wrapper_lines.append("}")
    elif filename.lower().endswith((".cbl", ".cob")):
        wrapper_lines.append(f"      * Strangler Fig facade for {class_name} - COBOL paragraphs below are candidates for extraction.")
        wrapper_lines.append(f"      * COBOL does not support object-style facades - this lists the paragraphs found so you can plan a manual extraction/PERFORM-based routing strategy.")
        for fn in funcs:
            wrapper_lines.append(f"      * - {fn}")
    if not wrapper_lines or not funcs:
        return {{"wrapper_generated": False, "wrapper_code": "", "functions_wrapped": [], "strangler_summary": "No functions found to wrap - nothing to generate a facade for.", "strangler_disclaimer": "Generates a Strangler Fig facade/adapter that delegates to legacy functions, letting you swap in new implementations incrementally without a full rewrite. Review and adapt the generated skeleton before use - it does not run or validate the legacy functions themselves."}}
    wrapper_code = chr(10).join(wrapper_lines)
    _truncation_note = f" ({{len(funcs_full) - 15}} more function(s) found but not wrapped - facade limited to the first 15 for readability)" if funcs_truncated else ""
    return {{"wrapper_generated": True, "wrapper_code": wrapper_code, "functions_wrapped": funcs, "total_functions_found": len(funcs_full), "functions_truncated": funcs_truncated, "strangler_summary": f"Generated a facade wrapping {{len(funcs)}} function(s){{_truncation_note}} - toggle use_new_impl per function as you build replacements.", "strangler_disclaimer": "Generates a Strangler Fig facade/adapter that delegates to legacy functions, letting you swap in new implementations incrementally without a full rewrite. Review and adapt the generated skeleton before use - it does not run or validate the legacy functions themselves."}}

'''

    before = content[:start_idx]
    after = content[end_idx+1:]
    content = before + new_function + after

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("REWRITE-COMPLETE")
else:
    print("FAILED-anchor-not-found")
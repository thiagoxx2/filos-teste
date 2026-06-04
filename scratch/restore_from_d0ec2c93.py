import os
import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d0ec2c93-74d2-477a-8e59-d52eadea87f7/.system_generated/logs/transcript.jsonl"

recovered_js = {}
recovered_css = {}

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get("content", "")
            if data.get("type") == "VIEW_FILE" and content:
                if "generate_responsive.js" in content:
                    lines = content.split("\n")
                    showing_line = -1
                    for idx, l in enumerate(lines):
                        if "Showing lines" in l:
                            showing_line = idx
                            break
                    if showing_line != -1:
                        for l in lines[showing_line+2:]:
                            if l.startswith("The above content"):
                                break
                            colon_idx = l.find(":")
                            if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                line_num = int(l[:colon_idx])
                                line_text = l[colon_idx+2:]
                                recovered_js[line_num] = line_text
                                
                if "responsive.css" in content:
                    lines = content.split("\n")
                    showing_line = -1
                    for idx, l in enumerate(lines):
                        if "Showing lines" in l:
                            showing_line = idx
                            break
                    if showing_line != -1:
                        for l in lines[showing_line+2:]:
                            if l.startswith("The above content"):
                                break
                            colon_idx = l.find(":")
                            if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                line_num = int(l[:colon_idx])
                                line_text = l[colon_idx+2:]
                                recovered_css[line_num] = line_text
        except Exception as e:
            pass

print(f"JS lines recovered: {len(recovered_js)}")
max_js = max(recovered_js.keys()) if recovered_js else 0
print(f"Max JS line: {max_js}")
missing_js = [i for i in range(1, max_js+1) if i not in recovered_js]
print(f"Missing JS lines count: {len(missing_js)}")
if missing_js:
    print("Missing JS lines:", missing_js[:50])

print(f"CSS lines recovered: {len(recovered_css)}")
max_css = max(recovered_css.keys()) if recovered_css else 0
print(f"Max CSS line: {max_css}")
missing_css = [i for i in range(1, max_css+1) if i not in recovered_css]
print(f"Missing CSS lines count: {len(missing_css)}")
if missing_css:
    print("Missing CSS lines:", missing_css[:50])

# Fallback clean HEAD file mapping for missing JS
head_js_file = "/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js"
with open(head_js_file, "r", encoding="utf-8") as f:
    head_js_lines = f.readlines()

reconstructed_js = []
for i in range(1, max_js + 1):
    if i in recovered_js:
        reconstructed_js.append(recovered_js[i])
    elif i <= len(head_js_lines):
        reconstructed_js.append(head_js_lines[i - 1].rstrip("\r\n"))
    else:
         reconstructed_js.append("")

with open("/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js", "w", encoding="utf-8") as out:
    out.write("\n".join(reconstructed_js))

print("Successfully wrote reconstructed generate_responsive.js!")

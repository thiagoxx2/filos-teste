import os
import json

brain_dir = "/Users/shayenefreita/.gemini/antigravity-ide/brain"
recovered_lines = {}

for folder in os.listdir(brain_dir):
    folder_path = os.path.join(brain_dir, folder)
    if not os.path.isdir(folder_path) or folder == "tempmediaStorage":
        continue
    
    log_file = os.path.join(folder_path, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(log_file):
        continue
        
    with open(log_file, "r", encoding="utf-8") as f:
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
                                    recovered_lines[line_num] = line_text
            except Exception as e:
                pass

print(f"Total unique JS lines recovered: {len(recovered_lines)}")
max_line = max(recovered_lines.keys()) if recovered_lines else 0
print(f"Max line number: {max_line}")

missing = []
for i in range(1, max_line + 1):
    if i not in recovered_lines:
        missing.append(i)
print(f"Number of missing lines: {len(missing)}")
if missing:
    print("Missing lines:", missing[:50])
else:
    # Write reconstructed JS to file
    js_content = "\n".join([recovered_lines[i] for i in sorted(recovered_lines.keys())])
    with open("/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js", "w", encoding="utf-8") as out:
        out.write(js_content)
    print("Successfully wrote reconstructed generate_responsive.js!")

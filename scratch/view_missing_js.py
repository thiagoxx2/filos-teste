import json

# Let's load the recovered lines from all logs
brain_dir = "/Users/shayenefreita/.gemini/antigravity-ide/brain"
recovered_lines = {}

for folder in os.listdir(brain_dir) if 'os' in globals() else []:
    pass

# We can just import os here
import os
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

print("Recovered lines around 440-530:")
for i in range(430, 540):
    if i in recovered_lines:
        print(f"{i}: {recovered_lines[i]}")
    else:
        print(f"{i}: MISSING")

print("\nHEAD generate_responsive.js lines 400-470:")
try:
    with open("/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js", "r") as f:
        head_lines = f.readlines()
    for idx, l in enumerate(head_lines[400:470]):
        print(f"{idx+401}: {l.strip()}")
except Exception as e:
    print("Error reading HEAD file:", e)

import os
import json

brain_dir = "/Users/shayenefreita/.gemini/antigravity-ide/brain"
found_css = []
found_js = []

for folder in os.listdir(brain_dir):
    folder_path = os.path.join(brain_dir, folder)
    if not os.path.isdir(folder_path) or folder == "tempmediaStorage":
        continue
    
    log_file = os.path.join(folder_path, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(log_file):
        continue
        
    print(f"Checking {folder}...")
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                step = data.get("step_index")
                content = data.get("content", "")
                if data.get("type") == "VIEW_FILE" and content:
                    if "responsive.css" in content:
                        lines = content.split("\n")
                        showing_line = -1
                        for idx, l in enumerate(lines):
                            if "Showing lines" in l:
                                showing_line = idx
                                break
                        if showing_line != -1:
                            # Parse lines
                            file_lines = []
                            for l in lines[showing_line+2:]:
                                if l.startswith("The above content"):
                                    break
                                colon_idx = l.find(":")
                                if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                    file_lines.append((int(l[:colon_idx]), l[colon_idx+2:]))
                            if file_lines:
                                found_css.append((folder, step, file_lines[0][0], file_lines[-1][0], file_lines))
                    
                    if "generate_responsive.js" in content:
                        lines = content.split("\n")
                        showing_line = -1
                        for idx, l in enumerate(lines):
                            if "Showing lines" in l:
                                showing_line = idx
                                break
                        if showing_line != -1:
                            # Parse lines
                            file_lines = []
                            for l in lines[showing_line+2:]:
                                if l.startswith("The above content"):
                                    break
                                colon_idx = l.find(":")
                                if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                    file_lines.append((int(l[:colon_idx]), l[colon_idx+2:]))
                            if file_lines:
                                found_js.append((folder, step, file_lines[0][0], file_lines[-1][0], file_lines))
            except Exception as e:
                pass

print(f"\n--- CSS VIEWS FOUND: {len(found_css)} ---")
for f, s, start, end, _ in found_css:
    print(f"Folder: {f}, Step: {s}, Lines: {start} to {end}")

print(f"\n--- JS VIEWS FOUND: {len(found_js)} ---")
for f, s, start, end, _ in found_js:
    print(f"Folder: {f}, Step: {s}, Lines: {start} to {end}")

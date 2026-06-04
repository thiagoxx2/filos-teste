import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

responsive_css_pieces = []
generate_responsive_js_pieces = []

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            content = data.get("content", "")
            
            # Check for view_file outputs
            if data.get("type") == "VIEW_FILE" and content:
                if "css/responsive.css" in content or "responsive.css" in content:
                    lines = content.split("\n")
                    # Extract the lines after "Showing lines X to Y"
                    showing_line = -1
                    for idx, l in enumerate(lines):
                        if "Showing lines" in l:
                            showing_line = idx
                            break
                    if showing_line != -1:
                        file_lines = []
                        for l in lines[showing_line+2:]:
                            if l.startswith("The above content"):
                                break
                            # remove line number prefix like "210: "
                            colon_idx = l.find(":")
                            if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                file_lines.append((int(l[:colon_idx]), l[colon_idx+2:]))
                        responsive_css_pieces.append((step, file_lines))
                        print(f"CSS View at Step {step}: lines {file_lines[0][0]} to {file_lines[-1][0]}")

                if "generate_responsive.js" in content:
                    lines = content.split("\n")
                    showing_line = -1
                    for idx, l in enumerate(lines):
                        if "Showing lines" in l:
                            showing_line = idx
                            break
                    if showing_line != -1:
                        file_lines = []
                        for l in lines[showing_line+2:]:
                            if l.startswith("The above content"):
                                break
                            colon_idx = l.find(":")
                            if colon_idx != -1 and l[:colon_idx].strip().isdigit():
                                file_lines.append((int(l[:colon_idx]), l[colon_idx+2:]))
                        generate_responsive_js_pieces.append((step, file_lines))
                        print(f"JS View at Step {step}: lines {file_lines[0][0]} to {file_lines[-1][0]}")
                        
        except Exception as e:
            pass

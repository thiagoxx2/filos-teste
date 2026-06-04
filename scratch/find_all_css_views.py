import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

recovered_lines = {}

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get("content", "")
            if data.get("type") == "VIEW_FILE" and content:
                if "css/responsive.css" in content or "responsive.css" in content:
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

print(f"Total unique lines recovered: {len(recovered_lines)}")
# Check for missing lines
missing = []
max_line = max(recovered_lines.keys()) if recovered_lines else 0
print(f"Max line number: {max_line}")

for i in range(1, max_line + 1):
    if i not in recovered_lines:
        missing.append(i)

print(f"Number of missing lines: {len(missing)}")
if missing:
    # group missing lines into ranges
    ranges = []
    start = missing[0]
    prev = missing[0]
    for m in missing[1:]:
        if m == prev + 1:
            prev = m
        else:
            ranges.append((start, prev))
            start = m
            prev = m
    ranges.append((start, prev))
    print("Missing ranges:", ranges)

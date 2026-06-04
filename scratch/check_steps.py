import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if 885 <= step <= 900:
                print(f"--- Step {step} ---")
                print("Type:", data.get("type"))
                print("Source:", data.get("source"))
                if "tool_calls" in data:
                    for call in data["tool_calls"]:
                        print("  Call:", call.get("name"), "args:", call.get("args"))
                if "content" in data:
                    print("  Content preview:", data["content"][:150].replace('\n', ' '))
        except Exception as e:
            pass

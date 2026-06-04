import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step in [23, 24]:
                print(f"--- Step {step} ---")
                print("Type:", data.get("type"))
                if "content" in data:
                    print("Length:", len(data["content"]))
                    print("Preview:", data["content"][:200])
        except Exception as e:
            pass

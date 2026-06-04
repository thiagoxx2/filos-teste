import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d0ec2c93-74d2-477a-8e59-d52eadea87f7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if step in [841, 842]:
                print(f"--- Step {step} ---")
                print("Type:", data.get("type"))
                if "content" in data:
                    print("Length:", len(data["content"]))
                    print("Preview:", data["content"][:300].replace('\n', ' '))
        except Exception as e:
            pass

import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get("step_index") == 983:
                # print keys or check where it has code content
                print("Step 983 keys:", data.keys())
                print("Step 983 type:", data.get("type"))
                # let's save the whole step json so we can inspect it
                with open("scratch/step_983.json", "w") as out:
                    json.dump(data, out, indent=2)
                print("Saved step 983 to scratch/step_983.json")
        except Exception as e:
            print("Error parsing:", e)

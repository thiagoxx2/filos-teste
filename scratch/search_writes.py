import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            tool_calls = data.get("tool_calls", [])
            for call in tool_calls:
                name = call.get("name")
                if name == "write_to_file":
                    args = call.get("args", {})
                    target = args.get("TargetFile", "")
                    print(f"Step {step}: write_to_file to {target}")
        except Exception as e:
            pass

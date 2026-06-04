import json

log_path = "/Users/shayenefreita/.gemini/antigravity-ide/brain/d810dbc7-9ccd-46b3-a074-c05fed1973e7/.system_generated/logs/transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            step = data.get("step_index")
            if 805 <= step <= 830:
                print(f"--- Step {step} ---")
                print("Keys:", data.keys())
                print("Type:", data.get("type"))
                # If there are tool calls, print them
                for call in data.get("tool_calls", []):
                    print("  Tool Call:", call.get("name"), "args:", call.get("arguments"))
                # If this is a tool response/status step, print output length
                if "content" in data:
                    print("  Content length:", len(data["content"]))
                    # print first 100 chars
                    print("  Content preview:", data["content"][:100].replace('\n', ' '))
        except Exception as e:
            pass

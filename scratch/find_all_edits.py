import os
import json

brain_dir = "/Users/shayenefreita/.gemini/antigravity-ide/brain"
edits = []

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
                step = data.get("step_index")
                tool_calls = data.get("tool_calls", [])
                for call in tool_calls:
                    name = call.get("name")
                    if name in ["replace_file_content", "multi_replace_file_content", "write_to_file"]:
                        args = call.get("args", {})
                        target = args.get("TargetFile", "")
                        if "responsive.css" in target or "generate_responsive" in target:
                            # Extract chunks/details
                            chunks = []
                            if name == "replace_file_content":
                                chunks.append({
                                    "StartLine": int(args.get("StartLine", 1)),
                                    "EndLine": int(args.get("EndLine", 1)),
                                    "TargetContent": args.get("TargetContent", ""),
                                    "ReplacementContent": args.get("ReplacementContent", "")
                                })
                            elif name == "multi_replace_file_content":
                                chunks_arg = args.get("ReplacementChunks", [])
                                # ReplacementChunks is a JSON list
                                for c in chunks_arg:
                                    chunks.append({
                                        "StartLine": int(c.get("StartLine", 1)),
                                        "EndLine": int(c.get("EndLine", 1)),
                                        "TargetContent": c.get("TargetContent", ""),
                                        "ReplacementContent": c.get("ReplacementContent", "")
                                    })
                            elif name == "write_to_file":
                                chunks.append({
                                    "CodeContent": args.get("CodeContent", "")
                                })
                            edits.append({
                                "folder": folder,
                                "step": step,
                                "action": name,
                                "target": target,
                                "chunks": chunks
                            })
            except Exception as e:
                pass

print(f"Total edits found: {len(edits)}")
# Sort edits by time/folder? Wait, how can we order the conversations chronologically?
# We can check folder creation/modification time!
edits_with_time = []
for e in edits:
    f_path = os.path.join(brain_dir, e["folder"])
    mtime = os.path.getmtime(f_path)
    edits_with_time.append((mtime, e))

edits_with_time.sort(key=lambda x: (x[0], x[1]["step"]))

for mtime, e in edits_with_time:
    print(f"Time: {mtime}, Folder: {e['folder']}, Step: {e['step']}, Action: {e['action']}, Target: {e['target']}")
    if "write_to_file" in e["action"]:
        print(f"  Writes file of length: {len(e['chunks'][0]['CodeContent'])}")
    else:
        print(f"  Modifies {len(e['chunks'])} chunks")
        for idx, chunk in enumerate(e["chunks"]):
            print(f"    Chunk {idx}: lines {chunk.get('StartLine')} to {chunk.get('EndLine')} (target len: {len(chunk.get('TargetContent', ''))} -> repl len: {len(chunk.get('ReplacementContent', ''))})")

import subprocess

blobs = [
    "3c8afa38f58ee5f99ee9794d7333b46b8bea25ed",
    "834b1b99889b4583bd4ec6777494f1edbf00f5a9",
    "6fbadeb32091b7ffa5b287e0581493d5f6cf8ff3"
]

for b in blobs:
    print(f"=== Blob {b} ===")
    try:
        content = subprocess.check_output(["git", "show", b], encoding="utf-8")
        lines = content.splitlines()
        print(f"Lines count: {len(lines)}")
        print("First 5 lines:")
        for l in lines[:5]:
            print("  ", l)
        print("Last 5 lines:")
        for l in lines[-5:]:
            print("  ", l)
    except Exception as e:
        print("Error:", e)

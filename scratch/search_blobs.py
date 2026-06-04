import subprocess
import re

try:
    # Run git fsck --unreachable
    output = subprocess.check_output(["git", "fsck", "--unreachable"], stderr=subprocess.DEVNULL, encoding="utf-8")
    blobs = []
    for line in output.splitlines():
        if "unreachable blob" in line:
            sha = line.split()[-1]
            # get size of blob
            size_out = subprocess.check_output(["git", "cat-file", "-s", sha], encoding="utf-8").strip()
            size = int(size_out)
            blobs.append((sha, size))
            
    # sort by size descending
    blobs.sort(key=lambda x: x[1], reverse=True)
    for sha, size in blobs[:30]:
        print(f"Blob: {sha}, size: {size}")
except Exception as e:
    print("Error:", e)

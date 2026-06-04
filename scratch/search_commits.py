import subprocess

try:
    output = subprocess.check_output(["git", "fsck", "--lost-found"], encoding="utf-8")
    for line in output.splitlines():
        if "commit" in line:
            print(line)
except Exception as e:
    print("Error:", e)

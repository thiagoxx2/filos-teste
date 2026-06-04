import os
import subprocess

objects_dir = "/Users/shayenefreita/FACULDADE FILOS/.git/objects"
matching_blobs = []

for root, dirs, files in os.walk(objects_dir):
    # Skip info and pack directories
    if "info" in root or "pack" in root:
        continue
    
    # Git objects are stored in subfolders named after the first two chars of SHA
    folder = os.path.basename(root)
    if len(folder) != 2:
        continue
        
    for f in files:
        sha = folder + f
        # check type of object
        try:
            obj_type = subprocess.check_output(["git", "cat-file", "-t", sha], encoding="utf-8").strip()
            if obj_type == "blob":
                size = int(subprocess.check_output(["git", "cat-file", "-s", sha], encoding="utf-8").strip())
                # If size matches or is close to our target sizes (45393 or 24189)
                if abs(size - 45393) < 4000 or abs(size - 24189) < 2000:
                    content = subprocess.check_output(["git", "cat-file", "-p", sha], encoding="utf-8")
                    if "responsive.css" in content:
                        matching_blobs.append((sha, size, "css", content))
                    if "generate_responsive" in content:
                        matching_blobs.append((sha, size, "js", content))
        except Exception as e:
            pass

print(f"Found {len(matching_blobs)} matching blobs:")
for sha, size, file_type, content in matching_blobs:
    print(f"SHA: {sha}, Size: {size}, Type: {file_type}")
    print("  Header preview:", content[:120].replace("\n", " "))
    # Save the largest CSS and JS as files to inspect or restore
    
css_blobs = [b for b in matching_blobs if b[2] == "css"]
js_blobs = [b for b in matching_blobs if b[2] == "js"]

if css_blobs:
    # sort by size descending and write largest
    css_blobs.sort(key=lambda x: x[1], reverse=True)
    best_css = css_blobs[0]
    with open("/Users/shayenefreita/FACULDADE FILOS/scratch/recovered_responsive.css", "w", encoding="utf-8") as out:
        out.write(best_css[3])
    print(f"Saved best CSS blob ({best_css[0]}) to scratch/recovered_responsive.css")

if js_blobs:
    js_blobs.sort(key=lambda x: x[1], reverse=True)
    best_js = js_blobs[0]
    with open("/Users/shayenefreita/FACULDADE FILOS/scratch/recovered_generate_responsive.js", "w", encoding="utf-8") as out:
        out.write(best_js[3])
    print(f"Saved best JS blob ({best_js[0]}) to scratch/recovered_generate_responsive.js")

import os

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"

for root, dirs, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if file == "index.html" and "filos-teste/index.html" not in file_path:
                # Add class="home" to index.html if it doesn't have it
                if "<body class=\"home\">" not in content and "<body>" in content:
                    content = content.replace("<body>", "<body class=\"home\">")
            else:
                # Remove class="internal-page"
                if "<body class=\"internal-page\">" in content:
                    content = content.replace("<body class=\"internal-page\">", "<body>")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

print("Done")

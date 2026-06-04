with open("/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# keep only first 1158 lines
truncated_lines = lines[:1158]

with open("/Users/shayenefreita/FACULDADE FILOS/generate_responsive.js", "w", encoding="utf-8") as f:
    f.writelines(truncated_lines)

print("Truncated generate_responsive.js to 1158 lines!")

with open("css/pages.css", "a", encoding="utf-8") as f:
    f.write("\n/* Ajustes finos visuais solicitados para compensar a largura do grid */\n")
    f.write("@media (max-width: 767px) {\n")
    f.write("  .home #cursos .filter-circle:nth-child(2) {\n")
    f.write("    margin-left: -3px;\n")
    f.write("  }\n")
    f.write("  .home #cursos .filter-circle:nth-child(4) {\n")
    f.write("    margin-left: 2px;\n")
    f.write("  }\n")
    f.write("}\n")

print("Fine-tuning appended.")

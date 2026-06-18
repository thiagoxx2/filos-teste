import re
import os

semesters = [
    ("1º SEMESTRE", [
        ("Anatomia Humana I", 60),
        ("Fundamentos de Psicologia e Enfermagem", 60),
        ("Responsabilidade Social e Meio Ambiente", 60),
        ("Fisiologia Humana", 60),
        ("Projeto Integrador I", 100),
        ("Leitura e Produção de Texto", 60),
    ]),
    ("2º SEMESTRE", [
        ("Posicionamento e Técnicas Radiológicas I", 60),
        ("Projeto Integrador II", 100),
        ("História e Equipamentos da Radiologia", 60),
        ("Matemática Básica e Física das Radiações", 60),
        ("Anatomia Humana II", 60),
        ("Metodologia do Trabalho Científico", 60),
    ]),
    ("3º SEMESTRE", [
        ("Ética e Legislação Aplicada à Radiologia", 60),
        ("Anatomia Humana III", 60),
        ("Exames Contrastados na Radiologia", 60),
        ("Imagionologia Digital Bioimagem I", 60),
        ("Posicionamento e Técnicas Radiológicas II", 60),
        ("Projeto Integrador III", 100),
    ]),
    ("4º SEMESTRE", [
        ("Imagionologia Digital Bioimagem II", 60),
        ("Projeto Integrador IV", 100),
        ("Tecnologia em RM, Radiologia Intervencionista e Hemodinâmica", 60),
        ("Proteção Radiológica e Radiobiologia", 60),
        ("Posicionamento e Técnicas Radiológicas III", 60),
        ("Tecnologia em Radioterapia e Radioisótopos", 60),
    ]),
    ("5º SEMESTRE", [
        ("Projeto Integrador V", 100),
        ("Estágio Supervisionado I", 250),
        ("Tecnologia em Mamografia e Densitometria Óssea", 60),
        ("Tecnologia em Medicina Nuclear", 60),
        ("Tecnologia em Tomografia Computadorizada", 60),
        ("Inglês e Informática Aplicada ao Diagnóstico", 60),
        ("Controle de Qualidade e Ultrassonografia", 60),
    ]),
    ("6º SEMESTRE", [
        ("Tecnologia em Ressonância Magnética", 60),
        ("Gestão Hospitalar e de Resíduos Hospitalares", 60),
        ("Tecnologia em Radiologia Veterinária", 60),
        ("Tecnologia em Radiologia Odontológica", 60),
        ("Tecnologia em Radiologia Industrial", 60),
        ("Projeto Integrador VI", 100),
        ("Estágio Supervisionado II", 250),
    ]),
]

# Generate HTML for accordions
accordions_html = ""
for idx, (sem_title, disciplines) in enumerate(semesters):
    accordions_html += f"""
            <!-- {sem_title} -->
            <div class="matriz-accordion-item">
              <button aria-expanded="false" class="matriz-accordion-header">
                <span>{sem_title}</span>
                <span class="accordion-icon"><i class="fa-solid fa-plus"></i></span>
              </button>
              <div class="matriz-accordion-content">
                <table class="matriz-table">
                  <thead>
                    <tr>
                      <th>DISCIPLINA</th>
                      <th class="text-center">H/A</th>
                    </tr>
                  </thead>
                  <tbody>
"""
    for disc_name, disc_hours in disciplines:
        accordions_html += f"""                    <tr>
                      <td>{disc_name}</td>
                      <td class="text-center">{disc_hours}</td>
                    </tr>
"""
    accordions_html += """                  </tbody>
                </table>
              </div>
            </div>"""

matriz_html = f"""
  <!-- --- MATRIZ CURRICULAR --- -->
  <section class="section section-matriz-admin">
    <!-- Marca d'água de fundo -->
    <div aria-hidden="true" class="matriz-watermark">FILOS</div>
    <div class="container matriz-container">
      <!-- Lado Esquerdo: Conteúdo e Acordeões -->
      <div class="matriz-left">
        <div class="matriz-header">
          <div class="matriz-icon-phi">
            <div class="matriz-phi-container">
              <img alt="Símbolo Faculdade Filos" class="matriz-phi-img" src="../assets/images/logo-faculdade-filos-oficial-white.png" />
            </div>
          </div>
          <h2 class="matriz-title">MATRIZ <strong>CURRICULAR</strong></h2>
          <p class="matriz-subtitle">Do curso de radiologia</p>
        </div>

        <div class="matriz-accordion">
{accordions_html}
        </div>
      </div>

      <!-- Lado Direito: Imagem -->
      <div class="matriz-right">
        <div class="matriz-student-image-wrapper">
          <img alt="Estudante de Radiologia - Faculdade Filos" class="matriz-student-img" src="../assets/images/student-pink-isolated.png" />
        </div>
      </div>
    </div>
  </section>
  <div class="matriz-footer-cta matriz-footer-cta--between">
    <a class="btn-matriz-enroll" href="https://wa.me/5561999061757">
      <i class="fa-brands fa-whatsapp"></i> MATRICULE-SE
    </a>
  </div>
"""

repo_dir = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE"

# 1. Extract CSS from administracao.html
with open(os.path.join(repo_dir, "cursos/administracao.html"), "r", encoding="utf-8") as f:
    admin_html = f.read()

# Find the CSS block
# From /* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- */ to </style>
css_match = re.search(r'(/\* --- ESTILOS SEÇÃO MATRIZ CURRICULAR --- \*/.*?</style>)', admin_html, re.DOTALL)
if css_match:
    matriz_css_block = css_match.group(1).replace("</style>", "").strip()
else:
    print("Could not find CSS block in administracao.html")
    matriz_css_block = ""

# 2. Inject CSS and HTML into radiologia.html
rad_path = os.path.join(repo_dir, "cursos/radiologia.html")
with open(rad_path, "r", encoding="utf-8") as f:
    rad_html = f.read()

# Check if already has CSS
if "section-matriz-admin" not in rad_html:
    # Inject CSS before </style>
    rad_html = rad_html.replace("</style>", f"\n    {matriz_css_block}\n  </style>")

# Check if already has HTML
if "MATRIZ CURRICULAR" not in rad_html:
    # Inject HTML before <section class="section section-related-courses"
    target = '<section class="section section-related-courses"'
    rad_html = rad_html.replace(target, matriz_html + "\n  " + target)

with open(rad_path, "w", encoding="utf-8") as f:
    f.write(rad_html)

print("Updated radiologia.html successfully.")

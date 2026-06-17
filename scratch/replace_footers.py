#!/usr/bin/env python3
import os
import re

ROOT = "/Users/shayenefreita/FACULDADE FILOS"

# Footer para páginas na raiz
FOOTER_ROOT = '''  <footer class="new-footer">
    <div class="container new-footer-grid">
      <!-- Col 1 -->
      <div class="new-footer-col new-footer-col-1">
        <div class="new-footer-col-top">
          <a href="index.html" aria-label="Ir para a home">
            <img src="assets/images/logo-faculdade-filos-oficial-white.png" alt="Logo Faculdade Filos" class="new-footer-logo">
          </a>
          <p class="new-footer-desc">
            A <strong>Faculdade Filos, reconhecida pelo MEC</strong>, oferece <strong>graduação, pós-graduação</strong> e
            cursos extensionistas com ensino de qualidade <strong>em Águas Lindas de Goiás</strong>. Com aulas noturnas e
            experiências práticas, prepara alunos para o mercado de trabalho.
          </p>
        </div>
        <div class="new-footer-location">
          <i class="fa-solid fa-location-dot"></i>
          <p>
            <span style="white-space: nowrap;">Avenida Tiradentes, Quadra 71, Lote 28/31,</span><br>
            <span style="white-space: nowrap;">Jardim Pérola - Barragem II, Águas Lindas de GO</span><br>
            <span style="white-space: nowrap;">CEP 72911-262</span>
          </p>
        </div>
      </div>

      <!-- Col 2 -->
      <div class="new-footer-col new-footer-col-2">
        <div class="new-footer-section">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> CURSOS</h4>
          <ul class="new-footer-links">
            <li><a href="#">Direito</a></li>
            <li><a href="#">Pedagogia</a></li>
            <li><a href="#">Radiologia</a></li>
            <li><a href="#">Administração</a></li>
          </ul>
        </div>

        <div class="new-footer-section new-footer-margin-top">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> CONTATO</h4>
          <ul class="new-footer-links new-footer-contact">
            <li><strong>WHATSAPP:</strong> 6199906-1757</li>
            <li><strong>TELEFONE:</strong> 3618-8111</li>
            <li>contato@faculdadefilos.com.br</li>
          </ul>
        </div>
      </div>

      <!-- Col 3 -->
      <div class="new-footer-col new-footer-col-3">
        <div class="new-footer-section">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> INSTITUCIONAL</h4>
          <ul class="new-footer-links">
            <li><a href="https://revistafaculdadefilos.com.br/index.php/ojs01" target="_blank"
                rel="noopener noreferrer">Revista</a></li>
            <li><a href="ouvidoria.html">Ouvidoria</a></li>
            <li><a href="cpa.html">CPA</a></li>
            <li><a href="biblioteca.html">Biblioteca</a></li>
            <li class="footer-link-divider"><a href="#" style="font-weight: 700; color: #ffffff;">Colégio</a></li>
            <li><a href="#">Portal do Aluno</a></li>
            <li><a href="#">Portal do professor</a></li>
          </ul>
        </div>

        <div class="new-footer-socials">
          <a href="#" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="new-footer-bottom">
      <div class="container">
        <p>Desenvolvido pela <a href="https://www.daraagencia.com/" target="_blank" rel="noopener noreferrer" class="footer-dara-link">agência Dara</a> | 2026</p>
      </div>
    </div>
  </footer>'''

# Footer para páginas em cursos/ (caminhos com ../)
FOOTER_CURSOS = '''  <footer class="new-footer">
    <div class="container new-footer-grid">
      <!-- Col 1 -->
      <div class="new-footer-col new-footer-col-1">
        <div class="new-footer-col-top">
          <a href="../index.html" aria-label="Ir para a home">
            <img src="../assets/images/logo-faculdade-filos-oficial-white.png" alt="Logo Faculdade Filos" class="new-footer-logo">
          </a>
          <p class="new-footer-desc">
            A <strong>Faculdade Filos, reconhecida pelo MEC</strong>, oferece <strong>graduação, pós-graduação</strong> e
            cursos extensionistas com ensino de qualidade <strong>em Águas Lindas de Goiás</strong>. Com aulas noturnas e
            experiências práticas, prepara alunos para o mercado de trabalho.
          </p>
        </div>
        <div class="new-footer-location">
          <i class="fa-solid fa-location-dot"></i>
          <p>
            <span style="white-space: nowrap;">Avenida Tiradentes, Quadra 71, Lote 28/31,</span><br>
            <span style="white-space: nowrap;">Jardim Pérola - Barragem II, Águas Lindas de GO</span><br>
            <span style="white-space: nowrap;">CEP 72911-262</span>
          </p>
        </div>
      </div>

      <!-- Col 2 -->
      <div class="new-footer-col new-footer-col-2">
        <div class="new-footer-section">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> CURSOS</h4>
          <ul class="new-footer-links">
            <li><a href="#">Direito</a></li>
            <li><a href="#">Pedagogia</a></li>
            <li><a href="#">Radiologia</a></li>
            <li><a href="#">Administração</a></li>
          </ul>
        </div>

        <div class="new-footer-section new-footer-margin-top">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> CONTATO</h4>
          <ul class="new-footer-links new-footer-contact">
            <li><strong>WHATSAPP:</strong> 6199906-1757</li>
            <li><strong>TELEFONE:</strong> 3618-8111</li>
            <li>contato@faculdadefilos.com.br</li>
          </ul>
        </div>
      </div>

      <!-- Col 3 -->
      <div class="new-footer-col new-footer-col-3">
        <div class="new-footer-section">
          <h4 class="new-footer-title"><span class="phi-symbol">&Phi;</span> INSTITUCIONAL</h4>
          <ul class="new-footer-links">
            <li><a href="https://revistafaculdadefilos.com.br/index.php/ojs01" target="_blank"
                rel="noopener noreferrer">Revista</a></li>
            <li><a href="../ouvidoria.html">Ouvidoria</a></li>
            <li><a href="../cpa.html">CPA</a></li>
            <li><a href="../biblioteca.html">Biblioteca</a></li>
            <li class="footer-link-divider"><a href="#" style="font-weight: 700; color: #ffffff;">Colégio</a></li>
            <li><a href="#">Portal do Aluno</a></li>
            <li><a href="#">Portal do professor</a></li>
          </ul>
        </div>

        <div class="new-footer-socials">
          <a href="#" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
          <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="new-footer-bottom">
      <div class="container">
        <p>Desenvolvido pela <a href="https://www.daraagencia.com/" target="_blank" rel="noopener noreferrer" class="footer-dara-link">agência Dara</a> | 2026</p>
      </div>
    </div>
  </footer>'''

def replace_footer(filepath, is_subdir):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    footer_new = FOOTER_CURSOS if is_subdir else FOOTER_ROOT

    # Substituir tudo entre <footer e </footer> inclusive
    new_content = re.sub(
        r'<footer[\s\S]*?</footer>',
        footer_new,
        content,
        flags=re.DOTALL
    )

    if new_content == content:
        print(f"  AVISO: nenhum <footer> encontrado em {filepath}")
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  OK: {filepath}")
    return True

# Páginas na raiz (excluindo index.html que já tem o footer correto)
root_pages = [
    "biblioteca.html", "cpa.html", "institucional.html",
    "ouvidoria.html", "politica-de-cookies.html",
    "politica-de-privacidade.html", "termos-de-uso.html"
]

print("=== Rodapé raiz ===")
for page in root_pages:
    path = os.path.join(ROOT, page)
    if os.path.exists(path):
        replace_footer(path, is_subdir=False)
    else:
        print(f"  NÃO ENCONTRADO: {page}")

# Páginas em cursos/
cursos_dir = os.path.join(ROOT, "cursos")
print("\n=== Rodapé cursos/ ===")
for fname in sorted(os.listdir(cursos_dir)):
    if fname.endswith(".html"):
        replace_footer(os.path.join(cursos_dir, fname), is_subdir=True)

print("\nConcluído.")

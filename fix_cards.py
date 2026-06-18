import re

path = "/Users/shayenefreita/FACULDADE FILOS - RESPONSIVIDADE/css/pages.css"
with open(path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace desktop CSS
desktop_old = r"\.diferencial-card-new \{.*?\.btn-diferencial-enroll:hover \{.*?\}"
desktop_new = """.diferencial-card-new {
  --card-scale: 1;
  background-color: #07162c;
  border-radius: calc(44px * var(--card-scale));
  padding: calc(2.6rem * var(--card-scale)) calc(2rem * var(--card-scale)) calc(3rem * var(--card-scale));
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  min-height: calc(340px * var(--card-scale));
  height: auto;
  transition: all var(--transition-normal);
  box-shadow: 0 10px 30px rgba(7, 22, 44, 0.15);
}

.diferencial-card-new:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(7, 22, 44, 0.35);
}

.diferencial-card-content {
  display: flex;
  flex-direction: column;
  gap: calc(1rem * var(--card-scale));
}

.diferencial-card-content--centered {
  flex: 1;
  justify-content: center;
}

.diferencial-card-title {
  font-family: var(--font-title);
  font-size: calc(1.75rem * var(--card-scale));
  font-weight: 800;
  color: var(--text-white);
  line-height: 1.15;
  word-break: normal;
  overflow-wrap: normal;
  hyphens: none;
}

.diferencial-card-desc {
  font-family: var(--font-body);
  font-size: calc(1.2rem * var(--card-scale));
  line-height: 1.35;
  color: #ffffff;
  font-weight: 400;
  margin-top: calc(2rem * var(--card-scale));
  word-break: normal;
  overflow-wrap: normal;
  hyphens: none;
}

.btn-diferencial-enroll {
  background-color: var(--cta-green);
  color: var(--text-white);
  border-radius: calc(50px * var(--card-scale));
  padding: calc(0.72rem * var(--card-scale)) calc(1.7rem * var(--card-scale));
  font-family: var(--font-title);
  font-weight: 700;
  font-size: calc(1.05rem * var(--card-scale));
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: calc(0.5rem * var(--card-scale));
  text-decoration: none;
  transition: all var(--transition-fast);
  position: absolute;
  bottom: calc(-16px * var(--card-scale));
  left: 50%;
  transform: translateX(-50%);
  width: fit-content;
  white-space: nowrap;
  box-shadow: 0 4px 10px rgba(7, 22, 44, 0.2);
  z-index: 2;
}

.btn-diferencial-enroll:hover {
  background-color: var(--cta-green-hover);
  transform: translateX(-50%) translateY(-2px);
  box-shadow: 0 6px 15px rgba(84, 152, 136, 0.4);
}"""

css = re.sub(desktop_old, desktop_new, css, flags=re.DOTALL)

# Replace mobile CSS
mobile_old = r"  \.diferencial-card-new \{.*?transform: translateX\(-50%\);\n  \}"
mobile_new = """  .diferencial-card-new {
    --card-scale: 0.85;
    width: min(100%, 360px);
    max-width: calc(100vw - 2rem);
  }
}

@media (max-width: 400px) {
  .diferencial-card-new {
    --card-scale: 0.78;
  }"""

css = re.sub(mobile_old, mobile_new, css, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(css)

print("Replacement done.")

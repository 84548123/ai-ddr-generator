from fpdf import FPDF

def generate_pdf(text, path):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Detailed Diagnostic Report", ln=True)

    pdf.set_font("Arial", size=10)

    for line in text.split("\n"):
        # ✅ REMOVE unsupported characters
        safe_line = line.encode("latin-1", "ignore").decode("latin-1")
        pdf.multi_cell(0, 6, safe_line)

    pdf.output(path)
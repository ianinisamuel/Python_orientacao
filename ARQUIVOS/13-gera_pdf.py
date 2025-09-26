from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Hello World", ln=True, align='C')
pdf.output("arquivos/dados/hello_world.pdf")
from fpdf import FPDF
import num2words
from datetime import date

# 1 - Variáveis

cliente = input("Nome do cliente: ")
consulta = input("Tipo de consulta: ")
vlr = input("Valor da consulta: ")
vlr_msg = f"{vlr} reais"
vlr_extenso = num2words.num2words(vlr, lang="pt_BR").capitalize() + " reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2 - Layout do PDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", size=20)
pdf.image("ARQUIVOS/dados/rec.jpg", x=0, y=0)
pdf.text(80,86, cliente)
pdf.text(162,45, vlr_msg)
pdf.text(80,108, vlr_extenso)
pdf.text(80,135, consulta)
pdf.set_text_color(255,255,255)
pdf.text(30,193, str(dia))
pdf.text(50,193, str(mes))
pdf.text(70,193, str(ano))
nome_arquivos = f"{cliente.strip().replace(' ', '_').lower()}_{dia}_{mes}_{ano}.pdf "
pdf.output(f"ARQUIVOS/dados/{nome_arquivos}.pdf")
print("PDF criado com sucesso!")
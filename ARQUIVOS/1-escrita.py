name = input("Digite seu nome:\n")
"""
- Arquivos:
1 - opção w - write (escrita)
2 - opção r - read (leitura)
3 - opção a - append (acrescentar)
"""

with open("names.txt", "a") as file:
	file.write(f"{name}\n")
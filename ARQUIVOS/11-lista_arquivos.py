import glob, os, zipfile

#1 - Diretorio de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos .txt
for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - Listar todos os arquivos .csv
for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - Compactar arquivos .txt
with zipfile.ZipFile("dados/text_files.zip", "w") as new_zip:
    for file in glob.glob("dados/*.txt"):
        new_zip.write(file, os.path.basename(file))

# 5 - Compactar todos arquivos
with zipfile.ZipFile("dados/all_files.zip", "w") as new_zip:
    for file in glob.glob("*.*"):
        new_zip.write(file, os.path.basename(file))
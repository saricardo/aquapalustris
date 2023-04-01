import os

if os.path.isfile("ENCOMENDA_FINAL.txt") == True:
    os.remove("ENCOMENDA_FINAL.txt")

orderfile = open("ENCOMENDA_FINAL.txt", "a", encoding="utf8",)

files =os.listdir('encomendas/')
#print(files)

for file in files:
    encomendafile = open("encomendas/"+file, "r", encoding="utf8",)
    encomendalines = encomendafile.readlines()
    orderfile.write("\n\n"+file+"\n\n")
    for line in encomendalines:
        orderfile.write(line)

print("Encomenda final pronta")
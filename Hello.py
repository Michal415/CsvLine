import csv
lista = []
with open("f:\\pliki\\zeszyt1.csv") as plik:
    odczyt =csv.reader(plik)
    for i in odczyt:
        if odczyt.line_num == 1:
            continue
        lista.append(i)
with open("f:\\pliki\\zapis.csv","w", newline='') as zapis2:
    zapis  =csv.writer(zapis2)
    for j in lista:
        zapis.writerow(j)

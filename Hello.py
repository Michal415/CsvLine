import csv
lista = []
with open("f:\\pliki\\zeszyt1.csv") as plik:
    odczyt =csv.reader(plik)
    for i in odczyt:
        if odczyt.line_num == 1:
            continue
        lista.append(i)
    zapis  =csv.writer(zapis2)
    zapis.writerows(lista)

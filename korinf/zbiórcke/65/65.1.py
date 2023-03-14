liczby = []
ulamki = []
m = 10000
with open('dane_ulamki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())


for i in range(len(liczby)):
    a = int(liczby[i].split()[0])/int(liczby[i].split()[1])
    ulamki.append(a)


for i in range(len(ulamki)):
    if ulamki[i] == min(ulamki):

        if int(liczby[i].split()[0])>m:
            pass
        else:
            m=int(liczby[i].split()[0])
            naji = i

print(liczby[naji])
liczby = []
wyn=0
with open('dane_napisy.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a = []
    b = []
    for j in range(len(liczby[i].split()[0])):

        a.append(liczby[i].split()[0][j])
        a.sort()


    for j in range(len(liczby[i].split()[1])):

        b.append(liczby[i].split()[1][j])
        b.sort()


    if a == b:
        wyn+=1
print(wyn)
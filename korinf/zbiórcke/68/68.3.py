liczby = []
max = 0
b = []

with open('dane_napisy.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a = []
    wyn = 0
    for j in range(len(liczby[i].split()[0])):

        a.append(liczby[i].split()[0][j])

    a.sort()
    for k in range(len(liczby)):
        for p in range(2):
            b = []
            for q in range(len(liczby[k].split()[p])):
                b.append(liczby[k].split()[p][q])

            b.sort()
            if b == a:
                wyn+=1

        if max<wyn:
            max = wyn

print(max)
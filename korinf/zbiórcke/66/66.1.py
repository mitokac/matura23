liczby = []

with open('trojki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a = 0
    for j in range(2):
        for k in range(len(liczby[i].split()[j])):
            a+=int(liczby[i].split()[j][k])

    if a==int(liczby[i].split()[2]):
        print(liczby[i])
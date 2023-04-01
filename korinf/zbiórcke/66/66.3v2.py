liczby = []
wyn = 0

with open('trojki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a = (int(liczby[i].split()[0]))*(int(liczby[i].split()[0])) + (int(liczby[i].split()[1]))*(int(liczby[i].split()[1]))
    a_1 = (int(liczby[i-1].split()[0]))*(int(liczby[i-1].split()[0])) + (int(liczby[i-1].split()[1]))*(int(liczby[i-1].split()[1]))
    if a == (int(liczby[i].split()[2]))*(int(liczby[i].split()[2])) and a_1 == (int(liczby[i-1].split()[2]))*(int(liczby[i-1].split()[2])):
        print(liczby[i])

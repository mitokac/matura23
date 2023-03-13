liczby = []
pierw = []
dziel = []

with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(int(line.strip()))

def czydziel(l, i):
    if l%i == 0:
        return True
    return False

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True






for i in range(2, 1000):
    if czy_pierwsza(i):
        pierw.append(i)

for i in range(len(liczby)):
    for j in range(2, 1000):
        if czydziel(liczby[i],j):
            if j%2!=0:
                if j in pierw:
                    dziel.append(j)
    if len(dziel) == 3:
        print(liczby[i])
        print(dziel)
        dziel.clear()
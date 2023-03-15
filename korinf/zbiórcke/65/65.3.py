liczby = []
licz = []
wyn = 0

with open('dane_ulamki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

def nwd(a, b):
    if b>0:
        return  nwd(b,a%b)
    return a


for i in range(len(liczby)):
    if nwd(int(liczby[i].split()[0]),int(liczby[i].split()[1]))==1:
        licz.append(liczby[i].split()[0])
        pass
    else:
        a = nwd(int(liczby[i].split()[0]),int(liczby[i].split()[1]))
        licz.append(str(int(liczby[i].split()[0])//a))


for i in range(len(licz)):
    wyn += int(licz[i])

print(wyn)
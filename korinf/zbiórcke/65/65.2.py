liczby = []
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
        wyn +=1

print(wyn)
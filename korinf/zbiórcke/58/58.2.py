fczas1 = []
fczas2 = []
fczas3 = []
tczas = 12
wyn = 0

with open('dane_systemy1.txt') as plik:
    for line in plik:
        fczas1.append(int(line.split()[0],2))
with open('dane_systemy2.txt') as plik:
    for line in plik:
        fczas2.append(int(line.split()[0],4))
with open('dane_systemy3.txt') as plik:
    for line in plik:
        fczas3.append(int(line.split()[0],8))

for i in range(len(fczas1)):
    tczas = 12 + i*24
    if fczas1[i]!=tczas and fczas2[i]!=tczas and fczas3[i]!=tczas:
        wyn+=1



print(wyn)
temp1 = []
temp2 = []
temp3 = []

with open('dane_systemy1.txt') as plik:
    for line in plik:
        temp1.append(int(line.split()[1],2))
with open('dane_systemy2.txt') as plik:
    for line in plik:
        temp2.append(int(line.split()[1],4))
with open('dane_systemy3.txt') as plik:
    for line in plik:
        temp3.append(int(line.split()[1],8))

a = bin(min(temp1))
print(a.replace('0b',''))
b = bin(min(temp2))
print(b.replace('0b',''))
c = bin(min(temp3))
print(c.replace('0b',''))


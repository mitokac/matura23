liczby10 = []
liczby8 = []
wyn10 = 0
wyn8=0

with open('liczby2.txt') as plik:
    for line in plik:
        liczby10.append(line.strip())
with open('liczby2.txt') as plik:
    for line in plik:
        liczby8.append(str(oct(int(line.strip()))))

for i in range(len(liczby10)):
    for j in range(len(liczby10[i])):
        if liczby10[i][j] == "6":
            wyn10 +=1

for i in range(len(liczby8)):
    for j in range(len(liczby8[i])):
        if liczby8[i][j] == "6":
            wyn8 +=1

print(wyn10)
print(wyn8)


#wyn8 i wyn10 powinny być odwrotnie idk czemu
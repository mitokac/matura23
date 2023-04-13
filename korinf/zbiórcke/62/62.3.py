liczby1 = []
liczby2 = []
wyna = 0
wynb = 0

with open('liczby1.txt') as plik:
    for line in plik:
        liczby1.append(int(line.strip(),8))
with open('liczby2.txt') as plik:
    for line in plik:
        liczby2.append(int(line.strip()))

for i in range(len(liczby1)):
    if liczby1[i]==liczby2[i]:
        wyna +=1

for i in range(len(liczby1)):
    if liczby1[i]>liczby2[i]:
        wynb +=1

print(wyna)
print(wynb)
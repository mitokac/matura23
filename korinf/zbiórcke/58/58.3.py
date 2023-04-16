temp1 = []
max1 = 0
temp2 = []
max2 = 0
temp3 = []
max3 = 0

czyRekord = False
wyn = 0

with open('dane_systemy1.txt') as plik:
    for line in plik:
        temp1.append(int(line.split()[1],2))
with open('dane_systemy2.txt') as plik:
    for line in plik:
        temp2.append(int(line.split()[1],4))
with open('dane_systemy3.txt') as plik:
    for line in plik:
        temp3.append(int(line.split()[1],8))

for i in range(len(temp3)):
    czyRekord = False

    if temp1[i] > max1:
        max1 = temp1[i]
        czyRekord = True

    if temp2[i] > max2:
        max2 = temp2[i]
        czyRekord = True

    if int(temp3[i]) > max3:
        max3 = temp3[i]
        czyRekord = True

    if czyRekord:
        wyn+=1

print(wyn)
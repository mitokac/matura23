import math

temp1 = []
max = 0

with open('dane_systemy1.txt') as plik:
    for line in plik:
        temp1.append(int(line.split()[1],2))

for i in range(len(temp1)):
    for j in range(len(temp1)):
        if i ==j:
            break
        r = (temp1[i]-temp1[j])**2
        skok = math.ceil(r/abs(i-j))
        if skok>max:
            max = skok

print(max)
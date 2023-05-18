piksele = []
max = 0
min = 300

with open('dane.txt') as plik:
    for line in plik:
        piksele.append(list(map(int,line.strip().split())))


for i in range(len(piksele)):
    for j in range(len(piksele[i])):
        if piksele[i][j]>max:
            max = piksele[i][j]
        if piksele[i][j]<min:
            min = piksele[i][j]

print(max)
print(min)
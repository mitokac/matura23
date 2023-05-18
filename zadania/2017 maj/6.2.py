piksele = []
wyw = 0

with open('dane.txt') as plik:
    for line in plik:
        piksele.append(list(map(int,line.strip().split())))

for i in range(len(piksele)):
    for j in range(len(piksele[i])//2):
        if piksele[i][j]!=piksele[i][319-j]:
            wyw+=1
            break

print(wyw)
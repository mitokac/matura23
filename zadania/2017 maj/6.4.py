piksele = []
max = 0
akt_ciag = 1

with open('dane.txt') as plik:
    for line in plik:
        piksele.append(list(map(int,line.strip().split())))

for i in range(320):
    akt_ciag = 1

    for j in range(199):
        if piksele[j][i] == piksele[j+1][i]:
            akt_ciag+=1
        else:
            if max < akt_ciag:
                max = akt_ciag

            akt_ciag=1

    if max<akt_ciag:
        max=akt_ciag

print(max)



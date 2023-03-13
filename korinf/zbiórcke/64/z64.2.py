obrazki = []
nierek=0
pierw = True
with open('dane_obrazki.txt') as plik:
    for i in range(200):
        obrazek = []

        for j in range(21):
            obrazek.append(plik.readline().strip())
        plik.readline()
        obrazki.append(obrazek)


for obrazek in obrazki:

    for i in range(10):
        for j in range(10):
            if obrazek[i][j] != obrazek[i+10][j] or obrazek[i][j] != obrazek[i][j+10] or obrazek[i][j] != obrazek[i+10][j+10]:
                break
        else:
            if pierw == True:
                for k in range(20):
                    for l in  range(20):
                        print(obrazek[k][l], end='')
                    print()
                pierw = False
            continue
        nierek += 1
        break

print(200-nierek)


obrazki = []
rew =0
maks = 0
def czy_par(line):
    cz = 0
    b = 0
    global maks
    for j in range(20):
        for i in range(20):
            if line[j][i] == '0':
                b +=1
            else:
                cz +=1
    if cz > maks:
        maks = cz
    return cz > b


with open('dane_obrazki.txt') as plik:
    for i in range(200):
        obrazek = []

        for j in range(21):
            obrazek.append(plik.readline().strip())
        plik.readline()
        obrazki.append(obrazek)
#
# for i in range(200):
#     for j in range(21):
#         print(obrazki[i][j])
#     print()
#     print()


for i in range(200):

    if czy_par(obrazki[i]):
        rew +=1
print(rew)
print(maks)


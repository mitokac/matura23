geny = []
wyn = 0
pj = 0
kj = 0

with open('dane_geny.txt') as plik:
    for line in plik:
        geny.append(line.strip())

for i in range(len(geny)):
    p = False
    k = False
    for j in range(len(geny[i])-1):
        if geny[i][j] == 'A' and geny[i][j+1] == 'A':
            # print(j)
            pj = j
            p = True
        if geny[i][j] == 'B' and geny[i][j+1] == 'B' and p:
            # print(j)
            kj = j
            k=True
        a = pj-kj
        if p and k and a>2 and pj<kj:
            p = False
            k = False
            # print(pj,kj)
            # print(a)
            wyn+=1


print(wyn)


#idk

# for i in range(len(geny)):
#     p = False
#     k = False
#     for j in range(len(geny[i])-1):
#         if geny[i][j] == 'A' and geny[i][j+1] == 'A':
#             print(j)
#             p = True
#         if geny[i][j] == 'B' and geny[i][j+1] == 'B' and p:
#             print(j)
#             k=True
#         if p and k:
#             p = False
#             k = False
#             wyn+=1
#             break

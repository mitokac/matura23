liczby = []
dz = []

def pierw(liczba):
    for j in range(len(dz)):
        if liczba % dz[j] == 0:
            return False

    return True

def nwd(l, l2):
    while l!=l2:
        if l>l2:
            l=l-l2
        else:
            l2=l2-l
    return l

with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(int(line.strip()))
for j in range(200):
    czy = False
    for i in range(200):
        if i!=j:
            if nwd(liczby[i], liczby[j]) != 1:
                czy = True
                break
    if not czy:
        dz.append(liczby[j])




# for i in range(200):
#     if pierw(liczby[i]):
#         print(liczby[i])


dz.sort()
print(dz)


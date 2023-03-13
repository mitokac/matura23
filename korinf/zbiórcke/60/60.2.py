liczby = []
ilo = 0

def funk(l):
    dz = []
    for j in range(1,l+1):
        if l%j == 0:
            dz.append(j)
    return dz

def funk2(l):
    dz = []
    d=1
    while d*d<l:
        if l%d ==0:
            dz.append(d)
            dz.append(l/d)

        d+=1

    if d*d ==l:
        dz.append(d)
    return dz

with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(int(line.strip()))

for i in range(1,200):
    x = funk2(liczby[i])
    if len(x) ==18:
        ilo+=1
        x.sort()
        print(x)


print(ilo)
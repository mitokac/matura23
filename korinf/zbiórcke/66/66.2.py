liczby = []

with open('trojki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

def pierw(l):
    for i in range(2,l):
        if l%i==0:
            return False
    return True


for i in range(len(liczby)):
    czyPierw=True

    if pierw(int(liczby[i].split()[0]))==False or pierw(int(liczby[i].split()[1])) == False:
        czyPierw = False

    if czyPierw and int(liczby[i].split()[0]) * int(liczby[i].split()[1]) == int(liczby[i].split()[2]):
        print(liczby[i])
liczby = []
wyn = 0

with open('trojki.txt') as plik:
    for line in plik:
        q = list(map(int,line.split()))
        liczby.append(q)

def czyProstokatny(l):
    a=l[0]
    b=l[1]
    c=l[2]
    if a**2+b**2 != c**2 and b**2+c**2 != a**2 and a**2+c**2 != b**2:
        return False
    return True



for i in range(1,len(liczby)):
    if czyProstokatny(liczby[i]) and czyProstokatny(liczby[i-1]):
        print(liczby[i])
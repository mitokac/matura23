liczby = []
ciag = 0
max = 0
with open('trojki.txt') as plik:
    for line in plik:
        q = list(map(int,line.split()))
        liczby.append(q)

def czyTroj(liczby):
    if liczby[0] + liczby[1] > liczby[2] and liczby[1] + liczby[2] > liczby[0] and liczby[2] + liczby[0] > liczby[1]:
        return True
    return False

for i in liczby:
    if czyTroj(i):
        ciag +=1
        if ciag > max:
            max = ciag
        continue
    ciag = 0

print(max)
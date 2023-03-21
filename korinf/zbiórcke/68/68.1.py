liczby = []


with open('dane_napisy.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a=[]
    b=[]
    for j in range(len(liczby[i].split()[0])):

        a.append(liczby[i].split()[0][j])

    for j in range(len(liczby[i].split()[1])):

        b.append(liczby[i].split()[1][j])
            
    if a==b:
        a.sort()
        b.sort()

        print(liczby[i])
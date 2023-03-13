liczby = []
a = ""
b=""

with open('ciagi.txt') as plik:
    for line in plik:
        liczby.append(str(line.strip()))


for i in range(len(liczby)):
    if len(liczby[i])%2 == 0:
        a = ""
        for j in range(len(liczby[i])//2):
            a = str(a) + str(liczby[i])[j]


        b = ""
        for k in range(len(liczby[i])//2,len(liczby[i])):
            b = b + str(liczby[i])[k]

        if a==b:
            print(liczby[i])

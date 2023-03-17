liczby = []
zero = 0
jeden = 0
wynik = 0

with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    for j in range(len(liczby[i])):
        if liczby[i][j] == "0":
            zero += 1
        else:
            jeden += 1
    if zero > jeden:
        wynik += 1
    zero = 0
    jeden = 0

print(wynik)

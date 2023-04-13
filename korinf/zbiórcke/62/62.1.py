liczby = []
with open('liczby1.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

print(min(liczby))
print(max(liczby))
print(int(min(liczby),8))
print(int(max(liczby),8))
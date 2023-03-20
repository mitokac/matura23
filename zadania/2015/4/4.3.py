liczby = []
liczbyd = []
najw = 0
najw_i = 0
najm = 1000
najm_i = 0

def bin2dec(l):
    return int(str(l),2)

with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(line.strip())


for i in range(len(liczby)):
    liczbyd.append(bin2dec(liczby[i]))

for i in range(len(liczby)):
    if bin2dec(liczby[i])>int(najw):
        najw = liczby[i]
        najw_i = i

    if bin2dec(liczby[i])<int(najm):
        najm = liczby[i]
        najm_i = i


print(liczbyd.index(max(liczbyd))+1)
print(liczbyd.index(min(liczbyd))+1)
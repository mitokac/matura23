liczby = []

przez2 = 0
przez8 = 0


with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

def bin2dec(l):
    return int(str(l),2)

for i in range(len(liczby)):
    if bin2dec(liczby[i])%2==0:
        przez2+=1

    if bin2dec(liczby[i])%8==0:
        przez8+=1

print(przez2)
print(przez8)
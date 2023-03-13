slowa = []
slowasz = []
k = 107

with open('dane_6_1.txt') as plik:
    for line in plik:
        slowa.append(plik.readline().strip())

for i in range(len(slowa)):
    slow = []
    for j in range(len(slowa[i])):
        if ord(slowa[i][j])+(k%26)<91:
            slow.append(chr(ord(slowa[i][j])+(k%26)))
        else:
            slow.append(chr(ord(slowa[i][j])+(k%26)-27))

    slowasz.append(slow)
print(slowasz)
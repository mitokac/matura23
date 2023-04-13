liczby = []
ciag = 0
max = 0
pierw = 0

with open('liczby2.txt') as plik:
    for line in plik:
        liczby.append(line.strip())


for i in range(len(liczby)-1):
    if liczby[i]<=liczby[i+1]:
        ciag+=1
        if max < ciag:
            max =ciag
            pierw = i - ciag
    elif liczby[i]>liczby[i+1]:
        ciag = 0
    else:
        print("-1")

print(max)
print(liczby[pierw])


#zły wynik idk
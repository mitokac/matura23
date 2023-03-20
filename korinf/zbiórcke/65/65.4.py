liczby = []
a=0
b=2^2*3^2*5^2*7^2*13
with open('dane_ulamki.txt') as plik:
    for line in plik:
        liczby.append(line.strip())

for i in range(len(liczby)):
    a+= int((liczby[i].split()[0])*b)//int(liczby[i].split()[1])

print(a//b)


#idk o co chodzi w tym zadaniu
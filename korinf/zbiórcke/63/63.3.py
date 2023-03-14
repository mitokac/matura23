liczby = []
wyn=[]

with open("ciagi.txt") as plik:
    for line in plik:
        liczby.append(int(line.strip(),2))

def pierwsza(l):
    for i in range(2,l-1):
        if l%i==0:
            return False
        return True

for i in range(len(liczby)):
    for j in range(2,liczby[i]):
        for k in range(2,liczby[i]):
            if pierwsza(j)==True and pierwsza(k)==True:
                if j*k==liczby[i]:
                    print(liczby[i])
                    break

                    

#idk czy działa, niezoptymalizowane
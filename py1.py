nom =[1, 2, 5, 10]
resz = []
kw = 500 - 123
nom.sort(reverse=True)
i=0


while kw > 0:

    if nom[i] <= kw:
        kw -= nom[i]
        resz.append(nom[i])
    else:
        i+=1

print(resz, sep=';')
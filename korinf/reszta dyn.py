mon = [1,2,4,5]
kw = 8
tab = [kw+1]*(kw+1)
#list comprehension

monety= [[0 for x in range(len(mon))].copy() for y in range(kw+1)]
#.copy
for x in monety:
    print(x)





    
tab[0]=0

for i in range(1,kw+1):
    for j in range(len(mon)):
        if mon[j]<=i:
            if tab[i-mon[j]]+1<tab[i]:
                tab[i] = tab[i - mon[j]] + 1
            # a = str(resz[x])
            # b = str(mon[j])
            # resz[i]=a + b
print(tab)


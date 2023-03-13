n = 15
j=0
# input(n)
sito = [1] * (n+1)
tab = []

sito[1]=0
sito[0]=0


for i in range(2,n):
    if sito[i]==1:
        j=i*i
        while j <= n:
            sito[j]=0
            j= j+i

for i in range(n):
    if sito[i]==1:
        tab.append(i)
print(tab)

a = 0
ciagi = []
max = 0
czyciag = True
ary=0

with open('ciagi.txt') as plik:
    for line in plik:
        a+=1
        if a%2==0:
            q = list(map(int, line.split()))
            ciagi.append(q)

for i in range(len(ciagi)):
    czyciag = True
    roznica = ciagi[i][1]-ciagi[i][0]

    for j in range(1,len(ciagi[i])-1):
        if ciagi[i][j] + roznica != ciagi[i][j+1]:
            czyciag = False
            break
    if czyciag== True:
        ary+=1
        if roznica>max:
            max = roznica

print(max)
print(ary)
ciagi = []
roznice = []
a = 0


with open('bledne.txt') as plik:
    for line in plik:
        a+=1
        if a%2==0:
            q = list(map(int, line.split()))
            ciagi.append(q)



for i in range(len(ciagi)):
    c=[]

    for j in range(len(ciagi[i])-1):
        c.append(ciagi[i][j+1]-ciagi[i][j])

    roznice.append(round(sum(c)/len(c)))

for i in range(len(ciagi)):

    for j in range(len(ciagi[i])):
        if ciagi[i][j] != ciagi[i][0]+j*roznice[i]:
            print(ciagi[i][j])
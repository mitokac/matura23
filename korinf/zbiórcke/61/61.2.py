import math

a=0
ciagi = []

def czySzescian(l):
    for i in range(l//3):
        if i*i*i == l or l==1:
            return True
    return False

with open('ciagi.txt') as plik:
    for line in plik:
        a+=1
        if a%2==0:
            q = list(map(int, line.split()))
            ciagi.append(q)



for i in range(len(ciagi)):
    for j in range(len(ciagi[i])-1,-1,-1):
        if czySzescian(ciagi[i][j]):
            print(ciagi[i][j])


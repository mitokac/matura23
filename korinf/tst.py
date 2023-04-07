l = [1,2,6,23,67,335]
p = 0
k=len(l)-1
x=5
sr=0

while p<=k:
    sr = (k+p)//2
    if l[sr]==x:
       print(sr)
       break
    if l[sr]>x:
        k=sr-1
    if l[sr]<x:
        p=sr+1

else:
    print("brak")
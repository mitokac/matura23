l = [1,2,6,23,67,335]
p = 0
k=len(l)-1
x=5
sr=0

def wysz(p,k,l):
    sr = (p+k)//2
    x = 5
    if l[sr] == x:
        return sr
    elif l[sr] > x:
        wysz(p, sr-1, l)
    elif l[sr] < x:
        wysz(sr+1,k,l)

# while p<=k:
#     sr = (k+p)//2
#     if l[sr]==x:
#        print(sr)
#        break
#     if l[sr]>x:
#         k=sr-1
#     if l[sr]<x:
#         p=sr+1
#
# else:
#     print("brak")
#


print(wysz(p,k,l))
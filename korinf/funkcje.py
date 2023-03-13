def silnia(x):
    wyn = 1
    while x > 1:
        wyn = wyn*x
        x-=1
    return wyn

def potega(a,b):
    wyn = 1
    for i in range(b):
        wyn = wyn*a
    return wyn

def silrek(a):
    if a == 0:
        return 1
    return a * silrek(a-1)

def potrek(a,b):
    if b ==0:
        return 1
    return a*potrek(a,b-1)

def fibb(n):
    a=1
    b=1
    for i in range(n-2):
        b=a+b
        a=b-a
    return b

def fibbrek(n):
    if n == 1 or n==2:
        return 1
    return fibbrek(n-1)+fibbrek(n-2)

def fibbdyn(n):
    l = [1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return l

def dectobinrek(l):

    if l>=1:
        dectobinrek(l//2)
        print(l%2)


def dectobin(l):
    while l>0:
        print(l%2)
        l = l//2


def bintodec2(l):
    p = 1
    sum =0
    for i in range(len(l)-1,-1,-1):
        print(int(l[i]))
        sum += (int(l[i])*p)
        p*=2
    return sum

def bintodec2(l,s):
    p = 1
    sum =0
    for i in range(len(l)-1,-1,-1):
        print(int(l[i]))
        sum += (int(l[i])*p)
        p*=s
    return sum



bintodec2("100101")

x=input()

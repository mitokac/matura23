
q = [121, 330, 990, 1331, 110, 225]
def nwd(a,b):
    c=0
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def nwd2(q):

    for i in range(len(q)-1):
        a=nwd(q[i],q[i+1])
        q[i+1] = a
        i+=1
    return a

def nwd3(q):
    for i in range(len(q)-1):
        a=q[i]
        b=q[i+1]
        while b != 0:
            r = a % b
            a = b
            b = r
        q[i+1]=a
        i+=1
    return a


print(nwd3(q))
wyw=0

def licz(x):
    global wyw
    wyw +=1
    if x == 1:
        return 1
    else:
        w = licz(x//2)
        if x%2==1:
            return w+1
        else:
            return w-1

for i in range(101,150):
    print(licz(i), i)
#print(wyw)
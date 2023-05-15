wyk = 0
i=int(input())
def wyniki(i):
    global wyk
    if i<3:
        return 1
    else:
        if i%2==0:
            wyk += 2

            return wyniki(i-3)+wyniki(i-1)+1
        else:
            wyk += 1

            return wyniki(i-1%7)

print(wyniki(i))
print(wyk)
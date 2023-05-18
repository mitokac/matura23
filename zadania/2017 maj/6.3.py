piksele = []
kont =0

with open('dane.txt') as plik:
    for line in plik:
        piksele.append(list(map(int,line.strip().split())))






for i in range(len(piksele)):

    for j in range(len(piksele[i])):
        if piksele[i][j]-piksele[i][max(0,j-1)]>128 or piksele[i][j]-piksele[i][max(0,j-1)]<-128:
            kont +=1
        elif piksele[i][j]-piksele[i][min(319,j+1)]>128 or piksele[i][j]-piksele[i][min(319,j+1)]<-128:
            kont +=1
        elif piksele[i][j]-piksele[max(0,i-1)][j]>128 or piksele[i][j]-piksele[max(0,i-1)][j]<-128:
            kont +=1
        elif piksele[i][j]-piksele[min(199,i+1)][j]>128 or piksele[i][j]-piksele[min(199,i+1)][j]<-128:
            kont +=1

print(kont)
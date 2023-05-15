obraz = []
a = 0
with open('dane.txt') as plik:
    for line in plik:
        obraz.append(list(map(int,line.strip().split())))


for i in range(1,len(obraz)-1):
    for j in range(1,len(obraz[i])-1):

        if abs(obraz[i][j]-obraz[i][j+1])>128:
            a+=1
        elif abs(obraz[i][j] - obraz[i -1][j]) > 128:
            a += 1
        elif abs(obraz[i][j]-obraz[i+1][j])>128:
            a+=1

        elif abs(obraz[i][j]-obraz[i-1][j])>128:
            a+=1



    if abs(obraz[0][i] - obraz[0][i+1]) > 128:
        a += 1
    elif abs(obraz[0][i] - obraz[0][i-1]) > 128:
        a += 1
    elif abs(obraz[0][i] - obraz[1][i]) > 128:
        a += 1

    if abs(obraz[199][i] - obraz[199][i + 1]) > 128:
        a += 1
    elif abs(obraz[199][i] - obraz[199][i-1]) > 128:
        a += 1
    elif abs(obraz[199][i] - obraz[199 - 1][i]) > 128:
        a += 1

    if abs(obraz[i][0] - obraz[i][1]) > 128:
        a += 1
    elif abs(obraz[i][0] - obraz[i+1][0]) > 128:
        a += 1
    elif abs(obraz[i][0] - obraz[i - 1][0]) > 128:
        a += 1

    if abs(obraz[i][319] - obraz[i][319-1]) > 128:
        a += 1
    elif abs(obraz[i][319] - obraz[i+1][319]) > 128:
        a += 1
    elif abs(obraz[i][319] - obraz[i - 1][319]) > 128:
        a += 1

    if abs(obraz[0][0] - obraz[0][1]) > 128:
        a += 1
    elif abs(obraz[0][0] - obraz[1][0]) > 128:
        a += 1
    if abs(obraz[199][0] - obraz[199][1]) > 128:
        a += 1
    elif abs(obraz[199][0] - obraz[199][0]) > 128:
        a += 1
    if abs(obraz[0][319] - obraz[0][318]) > 128:
        a += 1
    elif abs(obraz[0][319] - obraz[1][319]) > 128:
        a += 1
    if abs(obraz[199][319] - obraz[199][318]) > 128:
        a += 1
    elif abs(obraz[199][319] - obraz[198][319]) > 128:
        a += 1


print(a)
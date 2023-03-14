liczby = []
praw = True
wyn = []

with open('ciagi.txt') as plik:
    for line in plik:
        liczby.append(str(line.strip()))


for i in range(len(liczby)):
    praw = True
    for j in range(1,len(liczby[i])):
        if liczby[i][j] == liczby[i][j-1]:
            praw = False

    if praw == True:
        wyn.append(liczby[i])

print(len(wyn))
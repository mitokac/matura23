liczby = []
wtys = 0
mtys = []
post =0
ost = 0
with open('liczby.txt') as plik:
    for line in plik:
        liczby.append(int(line.strip()))


# for i in range(200):
#     if liczby[i] < 1000:
#         wtys +=1
#         mtys.append(liczby[i])
# #print(wtys)
# print(mtys[-2:])


for i in liczby:
    if i < 1000:
        post = ost
        ost = i
        wtys+=1

print(wtys)
print(post)
print(ost)

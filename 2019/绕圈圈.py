# -*- codeing: UTF-8 -*-

SIZE = 7
array = [[0] * SIZE]

print array

for i in range(SIZE - 1):
    array += [[0] * SIZE]

print array

orient = 0

j = 0
k = 0
for i in range(1, SIZE * SIZE + 1) :
    array[j][k] = i

    if j + k == SIZE - 1 :

        if j > k :
            orient = 1

        else :
            orient = 2

    elif (k == j) and (k >= SIZE / 2) :
        orient = 3

    elif (j == k - 1) and (k <= SIZE / 2) :
        orient = 0

    if orient == 0 :
        j += 1

    elif orient == 1:
        k += 1

    elif orient == 2:
        k -= 1

    elif orient == 3:
        j -= 1

for i in range(SIZE) :
    for j in range(SIZE) :
        print('%02d ' % array[i][j]+''),
    print("")
x = int(input())
y = int(input())

array1 = []
array2 = []

for i in range(x):
    row = []
    for j in range(y):
        row.append(int(input("".format(i + 1, j + 1))))
    array1.append(row)

array2 = [[0 for _ in range(x)] for _ in range(y)]

for i in range(x):
    for j in range(y):
        array2[j][i] = array1[i][j]

print(array2)
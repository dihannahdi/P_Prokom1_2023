x = int(input())
y = int(input())

array1 = []
array2 = []

for i in range(x):
    row = []
    for j in range(y):
        row.append(int(input("".format(i + 1, j + 1))))
    array1.append(row)

for i in range(x):
    row = []
    for j in range(y):
        row.append(int(input("".format(i + 1, j + 1))))
    array2.append(row)

for i in range(x):
    for j in range(y):
        array1[i][j] += array2[i][j]

print(array1)

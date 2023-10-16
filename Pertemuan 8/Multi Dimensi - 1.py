n = int(input())
for i in range(n):
    print()
    for j in range(n):
        if(i == j or i + j == n-1):
            print("1 ", end = "")
        elif(i != j):
            print("0 ", end = "")
        elif(j == n-1):
            print()


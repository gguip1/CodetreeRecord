N = int(input())

for i in range(N):
    n = N
    for j in range(i, -1, -1):
        print(n - j, end=' ')
    print()

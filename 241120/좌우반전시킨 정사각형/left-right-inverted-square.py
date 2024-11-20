n = int(input())

for i in range(1, n + 1):
    init_ = i
    for j in range(n, 0, -1):
        print((init_ * j), end=' ')
    print()
n = int(input())

list_ = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    if list_[i] % 2 == 0:
        print(list_[i], end=' ')

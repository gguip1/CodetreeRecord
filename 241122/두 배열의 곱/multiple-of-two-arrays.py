n = 3

arr_2d_1 = [
    list(map(int, input().split()))
    for i in range(n)
]

input()

arr_2d_2 = [
    list(map(int, input().split()))
    for i in range(n)
]

for i in range(3):
    for j in range(3):
        print(arr_2d_1[i][j] * arr_2d_2[i][j], end=' ')
    print()

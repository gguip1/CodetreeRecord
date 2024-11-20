n = int(input())

x = 1

for i in range(n, 0, -1):
    for j in range(i):
        print(f'{x} * {j + 1} = {x * (j + 1)}', end='')
        if j != i - 1:
            print(' / ', end='')
    print()
    x += 1
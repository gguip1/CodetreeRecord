n = int(input())

size = 2 * n - 1

t = 1

for j in range(n - 1, 0, -1):
    print(' ' * j, end='')
    print('* ' * t)
    t += 1

print('* ' * n)

t = n - 1
for j in range(1, n):
    print(' ' * j, end='')
    print('* ' * t)
    t -= 1
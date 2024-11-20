n = int(input())

t_0 = n + 1
t_1 = 0

for i in range(n):
    if i % 2 == 0:
        t_0 -= 1
        print('* ' * t_0)
    else:
        t_1 += 1
        print('* ' * t_1)

for i in range(n, 0, -1):
    if i % 2 == 0:
        t_0 -= 1
        print('* ' * t_0)
    else:
        t_1 += 1
        print('* ' * t_1)
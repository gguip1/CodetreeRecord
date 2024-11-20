n = int(input())

t_0 = n
t_1 = 1

for i in range(n):
    if i % 2 == 0:
        print('* ' * t_0)
        t_0 -= 1
    else:
        print('* ' * t_1)
        t_1 += 1

for i in range(n):
    if i % 2 == 0:
        print('* ' * t_0)
        t_0 -= 1
    else:
        print('* ' * t_1)
        t_1 += 1
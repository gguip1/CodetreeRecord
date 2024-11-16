op = input()
a_size = int(input())
a_ = list(map(int, input().split()))

for index, value in enumerate(op):
    if a_size > 0:
        if value == 'R':
            a_.reverse()
        elif value == 'D':
            a_.pop(0)
            a_size = len(a_)
    else:
        print('error')
        break

for i in a_:
    print(f'{i}', end=' ')

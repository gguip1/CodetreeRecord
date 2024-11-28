n = input()

def _(n):

    sum_ = 0

    for _ in n:
        sum_ += int(_)

    return int(n) % 2 == 0 and sum_ % 5 == 0

if _(n) == True:
    print('Yes')
else:
    print('No')

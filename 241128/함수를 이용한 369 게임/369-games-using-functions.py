a, b = map(int, input().split())

count = 0

def _(n):

    check = False

    for i in str(n):
        if i == '3' or i == '6' or i == '9':
            check = True
            break

    return n % 3 == 0 or check

for i in range(a, b + 1):
    if _(i) == True:
        count += 1

print(count)


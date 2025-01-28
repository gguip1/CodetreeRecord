N = int(input())

def ascending_nums(n):
    if n == 0:
        return
    ascending_nums(n - 1)
    print(n, end=' ')

def descending_nums(n):
    if n == 0:
        return
    print(n, end=' ')
    descending_nums(n - 1)

ascending_nums(N)
print()
descending_nums(N)

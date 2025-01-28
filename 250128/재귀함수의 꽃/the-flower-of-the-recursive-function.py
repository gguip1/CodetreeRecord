N = int(input())

def oteto(n):
    if n < 1:
        return
    print(n, end=' ')
    oteto(n - 1)
    print(n, end=' ')

oteto(N)

N = int(input())

check = True

def oteto(n):
    global check
    if n == 0:
        check = False
        n += 1
    elif n == N + 1 and not check:
        return
    
    if check:
        print(n, end=' ')
        oteto(n - 1)
    else:
        print(n, end=' ')
        oteto(n + 1)

oteto(N)

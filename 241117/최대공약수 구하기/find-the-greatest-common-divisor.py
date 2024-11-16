n, m = map(int, input().split())

def _print(n, m):
    max_ = 0
    if n > m:
        for i in range(n):
            if n % (i + 1) == 0 and m % (i + 1) == 0:
                max_ = (i + 1)
    else:
        for i in range(m ):
            if n % (i + 1) == 0 and m % (i + 1) == 0:
                max_ = (i + 1)
    
    print(max_)

_print(n, m)
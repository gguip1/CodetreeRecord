N = int(input())

def func(n, count=0):
    if n == 1:
        return count 
    else:
        count += 1
        if n % 2 == 0:
            return func(n // 2, count)
        else:
            return func(n // 3, count)

print(func(N))

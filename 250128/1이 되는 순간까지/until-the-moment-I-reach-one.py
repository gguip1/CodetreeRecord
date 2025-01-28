N = int(input())

count = 0

def func(n):
    global count
    if n == 1:
        return 
    else:
        count += 1
        if n % 2 == 0:
            func(n // 2)
        else:
            func(n // 3)

func(N)
print(count)

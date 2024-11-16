N = int(input())

def _print(N):
    num = 0
    for i in range(N):
        for j in range(N):
            num += 1
            if num % 10 == 0:
                num += 1
            print(num % 10, end=" ")
        print()

_print(N)

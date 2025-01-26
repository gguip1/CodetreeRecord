n, m = map(int, input().split())
arr = list(map(int, input().split()))

value = 0

while True:
    value += arr[m - 1]

    if m == 1:
        break

    if m % 2 == 0:
        m //= 2
    else:
        m -= 1

print(value)

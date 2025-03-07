a, b, c, d = map(int, input().split())

# Please write your code here.

minute = 0

while True:
    minute += 1
    b += 1

    if b == 60:
        a += 1
        b = 0

    if a == c and b == d:
        break

print(minute)
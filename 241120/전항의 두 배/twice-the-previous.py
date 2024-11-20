a, b = map(int, input().split())

c = a + b * 2

print(a, b, end=' ')

for i in range(8):
    c = b + 2 * a
    print(c, end=' ')
    a = b
    b = c

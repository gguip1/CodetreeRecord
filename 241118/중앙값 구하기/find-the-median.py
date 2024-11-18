a, b, c = map(int, input().split())

f_1 = a
f_2 = None
f_3 = None

if b > f_1:
    f_2 = f_1
    f_1 = b
else:
    f_2 = b

if c > f_1:
    f_3 = f_2
    f_2 = f_1
    f_1 = c
else:
    if c > f_2:
        f_3 = f_2
        f_2 = c
    else:
        f_3 = c

print(f_2)

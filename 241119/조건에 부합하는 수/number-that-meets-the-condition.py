a = int(input())

for i in range(a):
    value = i + 1
    if value % 2 == 0 and value % 4 != 0 or (value // 8) % 2 == 0 or value % 7 < 4:
        continue
    else:
        print(value, end=" ")
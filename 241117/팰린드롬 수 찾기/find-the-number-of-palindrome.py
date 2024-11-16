X, Y = map(int, input().split())

count = 0

for i in range(X, Y + 1):
    value = str(i)

    if len(value) % 2 == 0:
        if value[:len(value) // 2] == value[len(value) // 2:]:
            count += 1
    else:
        if value[:len(value) // 2] == value[len(value) // 2 + 1:]:
            count += 1

print(count)



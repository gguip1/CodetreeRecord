n = int(input())

count = 0

for i in range(n):
    n //= (i + 1)
    if n > 1:
        count += 1
    else:
        count += 1
        break
print(count)

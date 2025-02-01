a, b, c = map(int, input().split())

mul = a * b * c

result = 0

for s in str(mul):
    result += int(s)

print(result)

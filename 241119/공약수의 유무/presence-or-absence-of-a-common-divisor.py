a, b = map(int, input().split())

response = 0

for i in range(a, b + 1):
    if 1920 % i or 2880 % i:
        response = 1
        break

print(response)

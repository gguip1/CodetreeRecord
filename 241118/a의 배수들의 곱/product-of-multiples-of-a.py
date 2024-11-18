a, b = map(int, input().split())

prod = None

for i in range(1, b + 1):
    if prod is None:
        prod = 1
    if i % a == 0:
        prod *= i

if prod is None:
    prod = 0
    
print(prod)

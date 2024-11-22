n = 5
m = 3

arr = [
    list(input().split())
    for _ in range(n)
]

for _ in arr:
    for __ in _:
        print(__.upper(), end=' ')
    print()


n = 2
m = 4

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for _ in arr:
    print(f'{sum(_) / m:.1f}', end=' ')
print()


for i in range(m):
    sum_ = 0
    for j in range(n):
        sum_ += arr[j][i]
    print(f'{sum_ / n:.1f}', end=' ')
print()

sum_ = 0
for _ in arr:
    sum_ += sum(_)
print(f'{sum_ / (m * n):.1f}')
n = int(input())

result = []

for i in range(n):
    a, b = map(int, input().split())
    sum_ = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            sum_ += i
    result.append(sum_)

for v in result:
    print(v)
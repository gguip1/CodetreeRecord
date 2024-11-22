n = 4

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

sum_ = 0

for index, value in enumerate(arr):
    for i, v in enumerate(value):
        if i <= index:
            sum_ += v
        
print(sum_)

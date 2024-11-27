n = int(input())

arr_2d = [
    int(input())
    for _ in range(n)
]

sum_ = str(sum(arr_2d))

for index, value in enumerate(sum_):
    if index == 0:
        continue
    else:
        print(value, end='')

print(sum_[0])

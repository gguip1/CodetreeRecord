n = int(input())

arr_2d = [
    input()
    for _ in range(n)
]

sum_ = 0
count = 0

for _ in arr_2d:
    if _[0] == 'a':
        count += 1
    sum_ += len(_)

print(sum_, count)
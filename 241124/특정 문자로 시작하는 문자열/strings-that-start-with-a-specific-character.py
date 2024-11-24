n = int(input())

arr_2d = [
    input()
    for _ in range(n)
]

char_ = input()

count = 0
sum_ = 0

for _ in arr_2d:
    if _[0] == char_:
        count += 1
        sum_ += len(_)
    
print(count, f'{(sum_ / count) :.2f}')

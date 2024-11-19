sum_ = 0
count = 0

while(True):
    n = int(input())

    if n // 10 != 2:
        break
    else:
        sum_ += n
        count += 1

print(f'{(sum_/count):.2f}')
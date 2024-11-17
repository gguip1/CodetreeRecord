n, m = map(int, input().split())

_live = list(map(int, input().split()))

wifi_ = 0
sum_live = 0

for index, value in enumerate(_live):
    if value == 1 and sum_live < (1 + 2 * m):
        sum_live += 1
        if sum_live == (1 + 2 * m):
            wifi_ += 1
            sum_live = 0
    elif value == 0:
        wifi_ += 1


print(wifi_)


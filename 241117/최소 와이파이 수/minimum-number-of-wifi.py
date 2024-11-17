n, m = map(int, input().split())

_live = list(map(int, input().split()))

range_ = (1 + 2 * m)
index_ = n // range_

wifi_ = 0

for i in range(index_):
    c_0 = 0
    for j in _live[i * range_ : ((i + 1) * range_) - 1]:
        if j == 1:
            continue
        else:
            c_0 += 1
    if c_0 == range_:
        continue
    else:
        wifi_ += 1

print(wifi_)
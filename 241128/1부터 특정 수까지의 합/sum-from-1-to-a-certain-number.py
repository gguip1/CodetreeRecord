def _(num):
    sum_ = 0
    for i in range(num):
        sum_ += i + 1
    return sum_ // 10

N = int(input())

print(_(N))

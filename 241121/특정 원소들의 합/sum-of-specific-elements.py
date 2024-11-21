_ = []
for i in range(4):
    _.append(list(map(int, input().split())))

sum_ = 0

for i in range(4):
    for j in range(i + 1):
        sum_ += _[i][j]

print(sum_)

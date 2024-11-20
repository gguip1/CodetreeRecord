list_ = list(map(int, input().split()))

for i, v in enumerate(list_):
    if v % 3 == 0:
        print(list_[i - 1])
        break

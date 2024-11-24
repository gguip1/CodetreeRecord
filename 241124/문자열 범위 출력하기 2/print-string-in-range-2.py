str_ = input()
n = int(input())

if len(str_) < n:
    n = len(str_)

for i in range(len(str_) - 1, len(str_) - n - 1, -1):
    print(str_[i], end='')

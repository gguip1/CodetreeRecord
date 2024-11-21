n = int(input())
_ = list(map(int, input().split()))

min_ = None

for index, value in enumerate(_):
    if index < len(_) - 1:
        if min_ == None:
            min_ = _[index + 1] - value
        
        if min_ > (_[index + 1] - value):
            min_ = _[index + 1] - value

print(min_)

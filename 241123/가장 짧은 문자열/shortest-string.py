n = 3

arr = [
    input()
    for _ in range(n)
]

min_ = None
max_ = None

for _ in arr:
    if min_ == None or max_ == None:
        min_ = len(_)
        max_ = len(_)
    
    if max_ < len(_):
        max_ = len(_)

    if min_ > len(_):
        min_ = len(_)

print(max_ - min_)
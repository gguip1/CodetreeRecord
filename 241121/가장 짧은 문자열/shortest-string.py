max_ = None
min_ = None

for i in range(3):
    str_ = input()
    if max_ is None:
        max_ = len(str_)
    if min_ is None:
        min_ = len(str_)
    if len(str_) > max_:
        max_ = len(str_)
    if len(str_) < min_:
        min_ = len(str_)

print(max_ - min_)
_ = list(map(int, input().split()))

def min_(list_):
    min__ = None

    for __ in _:
        if min__ is None:
            min__ = __
            continue
        if min__ > __:
            min__ = __
        
        return min__

print(min_(_))




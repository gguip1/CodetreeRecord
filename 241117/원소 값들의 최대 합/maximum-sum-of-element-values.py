n, m = map(int, input().split())

_ = list(map(int, input().split()))

max_ = 0

for i in range(n):
    max__ = 0
    index = None
    for j in range(m):
        if index == None:
            index = i
            max__ += _[index]
            continue
            
        max__ += _[index - 1]
        index = _[index - 1]
    
    if max__ > max_:
        max_ = max__

print(max_)

n = int(input())

list_ = []

for i in range(n):
    if i == 0 or i == (n - 1):
        list__ = []
        for j in range(n):
            list__.append('*')
        list_.append(list__)
        continue

    list__ = []
    
    for z in range(i):
        list__.append('*')
    
    for z in range(n - i):
        if z == (n - i - 1):
            list__.append('*')
        else:
            list__.append(' ')

    list_.append(list__)

for v in list_:
    for v_ in v:
        print(v_, end=' ')
    print()

# 생각나는 대로
n, m = map(int, input().split())

_ = []
__ = []
for i in range(n):
    _.append(list(map(int, input().split())))

for i in range(n):
    __.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if _[i][j] == __[i][j]:
            _[i][j] = 0
        else:
            _[i][j] = 1

for i in range(n):
    for j in range(n):
        print(_[i][j], end=' ')
    print()

n = 10

arr_2d = [
    input()
    for _ in range(n)
]

char_ = input()

count = 0

for _ in arr_2d:
    if _[len(_) - 1] == char_:
        print(_)
        count += 1

if count == 0:
    print(None)

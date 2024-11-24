arr_2d = [
    "apple",
    "banana",
    "grape",
    "blueberry",
    "orange"
]

char_ = input()

count = 0

for _ in arr_2d:
    if _[2] == char_ or _[3] == char_:
        print(_)
        count += 1

print(count)

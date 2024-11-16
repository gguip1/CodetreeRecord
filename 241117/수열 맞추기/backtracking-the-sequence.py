n = int(input())
a = list(map(int, input().split()))
a.reverse()

result_array = []

for index, value in enumerate(a):
    if len(result_array) >= 1:
        if value == 1:
            result_array.insert(0, index + 1)
        elif value == 2:
            result_array.insert(1, index + 1)
        elif value == 3:
            result_array.append(index + 1)
    else:
        result_array.insert(0, index + 1)

for v in result_array:
    print(v, end=" ")
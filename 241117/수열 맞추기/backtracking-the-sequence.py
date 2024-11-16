n = int(input())
a = list(map(int, input().split()))
a.reverse()

result_array = [None] * n
size = 0

for index, value in enumerate(a):
    if value == 1:
        result_array[1:size+1] = result_array[0:size]
        result_array[0] = index + 1
    elif value == 2:
        result_array[2:size+1] = result_array[1:size]
        result_array[1] = index + 1
    elif value == 3:
        result_array[size] = index + 1
    size += 1

print(" ".join(map(str, result_array[:size])))

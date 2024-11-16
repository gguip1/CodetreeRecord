n = int(input())
a = list(map(int, input().split()))

array_ = []

for i in range(n):
    array_.append(i + 1)

a.reverse()
result_array = []

for index, value in enumerate(a):
    if len(result_array) >= 1:
        if value == 1:
            result_array.insert(0, array_[index])
        elif value == 2:
            result_array.insert(1, array_[index])
        elif value == 3:
            result_array.append(array_[index])
    else:
        result_array.insert(0, array_[index])

for index, value in enumerate(result_array):
    print(value, end=" ")
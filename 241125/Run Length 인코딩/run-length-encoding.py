A = input()

previous = ''
count = 0
result = ''

for index, _ in enumerate(A):
    if previous == '':
        previous = _
        count += 1
    elif previous == _:
        count += 1
    else:
        result += previous
        result += str(count)
        previous = _
        count = 1
    
    if index == len(A) - 1:
        result += previous
        result += str(count)

print(len(result))
print(result)
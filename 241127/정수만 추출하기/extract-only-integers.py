문자열_1, 문자열_2 = input().split()

def isInt(str_):
    if str_ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False

sum_ = 0

previous = ''

for i in range(len(문자열_1)):
    if isInt(문자열_1[i]):
        previous += 문자열_1[i]
        if i == len(문자열_1) - 1:
            sum_ += int(previous)
    else:
        if previous == '':
            continue
        else:
            sum_ += int(previous)
            previous = ''

previous = ''

for i in range(len(문자열_2)):
    if isInt(문자열_2[i]):
        previous += 문자열_2[i]
        if i == len(문자열_2) - 1:
            sum_ += int(previous)
    else:
        if previous == '':
            continue
        else:
            sum_ += int(previous)
            previous = ''

print(sum_)

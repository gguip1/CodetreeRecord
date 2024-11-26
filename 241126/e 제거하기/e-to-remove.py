str_ = input()

check = 0

for i in range(len(str_)):
    if str_[i] == 'e':
        check += 1
    if check == 1:
        check += 1
        continue
    print(str_[i], end='')


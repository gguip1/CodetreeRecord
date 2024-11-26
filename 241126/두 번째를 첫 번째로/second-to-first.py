str_ = input()

f = str_[0]
s = str_[1]

for i in range(len(str_)):
    if str_[i] == s:
        print(f, end='')
    else:
        print(str_[i], end='')
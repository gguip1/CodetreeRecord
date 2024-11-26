str_ = input()

for i in range(len(str_) - 1, -1, -1):
    if i % 2 != 0:
        print(str_[i],  end='')

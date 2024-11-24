str_ = 'hello'

for _ in str_:
    if _ == 'h':
        print(f'{_.upper()}', end='')
        continue
    print(f'{_}', end='')

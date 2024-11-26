c = input()

for i in range(len(c)):
    if ord(c[i]) > 91:
        print(c[i].upper(), end='')
    else:
        print(c[i].lower(), end='')

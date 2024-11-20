N = int(input())

code = 65

for i in range(N):
    for j in range(N):
        if j > (i - 1):
            print(chr(code), end=' ')
            code += 1
            if code > 90:
                code = 65
        else:
            print(' ', end=' ')
    print()

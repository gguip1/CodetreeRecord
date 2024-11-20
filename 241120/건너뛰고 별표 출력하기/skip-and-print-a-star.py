n = int(input())

for i in range(n):

    print('*' * (i + 1))

    print()

    if (i + 1) == n:

        for j in range(n - 1, 0, -1):

            print('*' * (j))

            print()
A = input()
C = input()

for i in range(len(C)):
    if C[i] == 'L':
        A = A[1:] + A[0]
    else:
        A = A[len(A) - 1] + A[:len(A) - 1]

print(A)

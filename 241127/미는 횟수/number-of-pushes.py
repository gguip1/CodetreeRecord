A = input()
B = input()

count = 0
check = False

for i in range(len(A)):
    A = A[len(A) - 1] + A[0:len(A) - 1] 
    count += 1
    if A == B:
        check = True
        break

if check == True:
    print(count)
else:
    print(-1)


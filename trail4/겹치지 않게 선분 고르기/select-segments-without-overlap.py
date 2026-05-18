n = int(input())
xy1 = []

for _ in range(n):
    a, b = map(int, input().split())
    xy1.append((a, b))

xy1.sort()

# Please write your code here.
answer = 0
xy2 = []

def backtracking(last_point):
    global answer
    for i in range(n):
        if last_point < xy1[i][0]:
            xy2.append(xy1[i])
            backtracking(xy1[i][1])
            xy2.pop()
        else:
            answer = max(answer, len(xy2))
    return 

backtracking(-1)
print(answer)

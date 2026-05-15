n = int(input())

# Please write your code here.

answer = 0

def backtracking(l:list):
    global answer
    if len(l) == n:
        answer += 1
        return
    
    if len(l) > n:
        return
    
    for i in range(1, 5):
        l.extend([i] * i)
        backtracking(l)
        for i in range(i):
            l.pop()


backtracking([])
print(answer)

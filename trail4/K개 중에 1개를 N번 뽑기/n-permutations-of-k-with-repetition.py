K, N = map(int, input().split())

# Please write your code here.

def backtracking(curNum):
    if len(curNum) == N:
        print(*curNum)
        return
    
    for i in range(1, K + 1):
        curNum.append(i)
        backtracking(curNum)
        curNum.pop()

backtracking([])

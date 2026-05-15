n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
bomb_pos = []
bomb_grid = [[0] * n for _ in range(n)]
bombed = [[False] * n for _ in range(n)]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

def calc():
    for y in range(n):
        for x in range(n):
            bombed[y][x] = False

    bomb_range = [
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [0, 1], [0, 0], [1, 0], [0, -1]],
        [[-1, -1], [-1, 1], [0, 0], [1, 1], [1, -1]]
    ]

    for y, x in bomb_pos:
        for ry, rx in bomb_range[bomb_grid[y][x] - 1]:
            if in_range(y + ry, x + rx):
                bombed[y + ry][x + rx] = True

    c = 0
    for y in range(n):
        for x in range(n):
            if bombed[y][x]:
                c += 1
    
    return c

def backtracking(cnt):
    global answer
    if cnt == len(bomb_pos):
        answer = max(answer, calc())
        return
    
    for i in range(1, 4):
        y, x = bomb_pos[cnt]

        bomb_grid[y][x] = i
        backtracking(cnt + 1)
        bomb_grid[y][x] = 0

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            bomb_pos.append((y, x))

backtracking(0)
print(answer)

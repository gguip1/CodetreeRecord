n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
d = {}

for i in range(1, n + 1):
    d[i] = []

for s, e in edges:
    d[s].append(e)
    d[e].append(s)

answer = 0

visited = [False] * (n + 1)

stack = [1]
visited[1] = True

while stack:
    n = stack.pop()

    for x in d[n]:
        if not visited[x]:
            stack.append(x)
            visited[x] = True
            answer += 1

print(answer)

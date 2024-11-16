from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.reverse()

result_deque = deque()

for index, value in enumerate(a):
    if value == 1:
        result_deque.appendleft(index + 1)  # 맨 앞에 삽입
    elif value == 2:
        result_deque.insert(1, index + 1)  # 두 번째에 삽입
    elif value == 3:
        result_deque.append(index + 1)  # 맨 뒤에 삽입

print(" ".join(map(str, result_deque)))

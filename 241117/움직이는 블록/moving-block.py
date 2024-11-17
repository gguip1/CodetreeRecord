N = int(input())

_list = []

for i in range(N):
    _list.append(int(input()))

avg = sum(_list) // len(_list)

# t_count = 0

# for i in range(N):
#     count = 0
#     while(True):        
#         if _list[i] < 5:
#             break
#         else:
#             _list[i] -= 1
#             count += 1
    
#     for j in range(count):
#         for z in range(N):
#             if _list[z] < 5:
#                 _list[z] += 1

c = 0

for i in range(N):
    if _list[i] - avg > 0:
        c += _list[i] - avg

print(c)

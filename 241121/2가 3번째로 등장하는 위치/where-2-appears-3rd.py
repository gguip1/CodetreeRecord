n = int(input())
_ = []
_ = list(map(int, input().split()))

count = 0
index_ = 0

for index, value in enumerate(_):
    if value == 2:
        count += 1
        index_ = index + 1
    
    if count == 3:
        break

print(index_)

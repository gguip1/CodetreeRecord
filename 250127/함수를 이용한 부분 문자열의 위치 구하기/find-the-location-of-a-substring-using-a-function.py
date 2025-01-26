string = input()
target = input()

start_index = 0

for i in range(len(string)):

    for j in range(len(target)):
        if string[i + j] == target[j]:
            start_index = i
        else:
            start_index = 0
            break
    
    if start_index != 0:
        break

if start_index != 0:
    print(start_index)
else:
    print(-1)
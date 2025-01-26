string = input()
target = input()

start_index = -1

for i in range(len(string)):

    for j in range(len(target)):
        if string[i + j] == target[j]:
            start_index = i
        else:
            start_index = -1
            break
    
    if start_index != -1:
        break

print(start_index)
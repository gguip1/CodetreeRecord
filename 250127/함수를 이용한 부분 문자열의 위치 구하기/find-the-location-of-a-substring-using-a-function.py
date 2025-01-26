string = input()
target = input()

start_index = -1

for i in range(len(string)):

    if len(string[i:]) >= len(target):
        for j in range(len(target)):
            if string[i + j] == target[j]:
                start_index = i
            else:
                start_index = -1
                break
    else:
        start_index = -1
    
    if start_index != -1:
        break

print(start_index)
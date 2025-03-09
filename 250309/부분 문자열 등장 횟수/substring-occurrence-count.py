T = input()
P = input()

# Please write your code here.

def makeTable(pattern:list):
    patternSize = len(pattern)

    table = [0] * patternSize

    j = 0
    for i in range(1, patternSize):
        while(j > 0 and pattern[i] != pattern[j]):
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    
    return table

def kvm(parent:list, pattern:list):
    parentSize = len(parent)
    patternSize = len(pattern)

    table = makeTable(pattern)

    count = 0

    j = 0
    for i in range(1, parentSize):
        while(j > 0 and parent[i] != pattern[j]):
            j = table[j - 1]
        if parent[i] == pattern[j]:
            j = table[j]
            count += 1
        else:
            j += 1
    
    return count

print(kvm(T, P))

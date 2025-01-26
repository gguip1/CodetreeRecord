string = input()

a = [0 for _ in range(ord('z') - ord('a') + 1)]

for s in list(string):
    a[ord(s) - ord('a')] += 1

count = 0

for _ in a:
    if _ != 0:
        count += 1

if count >= 2:
    print('Yes')
else:
    print('No')

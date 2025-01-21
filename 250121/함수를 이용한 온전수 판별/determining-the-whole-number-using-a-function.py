a, b = map(int, input().split())

# Write your code here!

def is_perfect_num(num):
    if num % 2 == 0:
        return False
    
    if num % 10 == 5:
        return False
    
    if num % 3 == 0 and num % 9 == 0:
        return False
    
    return True

count = 0

for i in range(a, b + 1):
    if is_perfect_num(i):
        count += 1

print(count)

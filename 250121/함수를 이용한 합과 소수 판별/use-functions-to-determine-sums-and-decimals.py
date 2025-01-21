a, b = map(int, input().split())

# Write your code here!
def is_prime(num):

    for i in range(num):

        if (i + 1) == 1 or (i + 1) == num:
            continue
        
        if num % (i + 1) == 0:
            return False
    
    return True

def is_sum_even(num):

    sum_ = 0

    for i in range(len(str(num))):

        sum_ += int(str(num)[i])

    if sum_ % 2 == 0:
        return True
    else:
        return False

count = 0

for i in range(a, b + 1):
        
    if is_prime(i) and is_sum_even(i):
        count += 1

print(count)

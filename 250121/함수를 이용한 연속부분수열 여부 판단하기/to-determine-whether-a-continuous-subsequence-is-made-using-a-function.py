n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Write your code here!
def check_list(x, y):
    for i in range(n2):
        if x[i] != y[i]:
            return False
    return True

result = "No"

if n1 == n2:
    if check_list(a, b):
            result = "Yes"
else:
    for i in range(n1 - n2):
        if check_list(a[i:i + n2], b):
            result = "Yes"
            break
        else:
            continue

print(result)
n, m = map(int, input().split())

# Write your code here!
def swap(a, b):
    temp = a
    a = b
    b = temp

    return a, b

n, m = swap(n, m)
print(n, m)

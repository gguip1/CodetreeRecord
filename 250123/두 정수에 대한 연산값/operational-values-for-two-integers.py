a, b = map(int, input().split())

# Write your code here!

def much_better_a(a, b):
    if a > b:
        return True
    else:
        return False

if much_better_a(a, b):
    print(a + 25, b * 2)
else:
    print(a * 2, b + 25)

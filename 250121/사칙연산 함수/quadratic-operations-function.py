a, o, c = input().split()
a = int(a)
c = int(c)

# Write your code here!
def sum_(x, y):
    return x + y

def sub_(x, y):
    return x - y

def div_(x, y):
    return x // y

def mul_(x, y):
    return x * y

if o == '+':
    print(f'{a} {o} {c} = {sum_(a, c)}')
elif o == '-':
    print(f'{a} {o} {c} = {sub_(a, c)}')
elif o == '/':
    print(f'{a} {o} {c} = {div_(a, c)}')
elif o == '*':
    print(f'{a} {o} {c} = {mul_(a, c)}')
else:
    print(False)

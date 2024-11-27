A = input()
B = input()

def isInt(str_):
    if str_ in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False

value_A = ''

for _ in A:
    if isInt(_):
        value_A += _

value_B = ''

for _ in B:
    if isInt(_):
        value_B += _

print(int(value_A) + int(value_B))

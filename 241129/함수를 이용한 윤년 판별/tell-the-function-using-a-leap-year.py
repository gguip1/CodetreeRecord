def is_year(n):
    if n % 4 != 0:
        return False
    if n % 100 == 0 and n % 400 != 0:
        return False
    return True

y = int(input())

result = 'true' if is_year(y) else 'false'

print(result )

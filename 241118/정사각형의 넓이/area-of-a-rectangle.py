n = int(input())

def ext(n):
    if n < 5:
        return 'tiny'
    return n * n

print(ext(n))
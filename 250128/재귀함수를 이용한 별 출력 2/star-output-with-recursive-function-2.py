N = int(input())

def print_stars(n):
    if n < 1:
        return
    
    print('* ' * n)
    print_stars(n - 1)
    print('* ' * n)

print_stars(N)

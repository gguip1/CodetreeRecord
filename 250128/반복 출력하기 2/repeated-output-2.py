N = int(input())

def print_helloWorld(N):
    if N == 0:
        return
    else:
        print('HelloWorld')
        N -= 1
        print_helloWorld(N)

print_helloWorld(N)

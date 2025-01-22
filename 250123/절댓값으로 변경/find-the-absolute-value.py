n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

def abs(arr):
    for index, value in enumerate(arr):
        if value < 0:
            arr[index] = -1 * arr[index]

abs(arr)

for val in arr:
    print(val, end=" ")

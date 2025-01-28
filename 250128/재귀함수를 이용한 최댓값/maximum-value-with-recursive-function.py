n = int(input())
nums = list(map(int, input().split()))

def max(index = 0, max_index=0):
    if index == n - 1:
        return max_index
    
    if nums[index] > nums[max_index]:
        return max(index + 1, index)
    else:
        return max(index + 1, max_index)

print(nums[max()])

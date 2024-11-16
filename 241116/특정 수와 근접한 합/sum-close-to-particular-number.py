N, S = map(int, input().split())

nums = list(map(int, input().split()))

best_diff = None
best_nums = []

for i in range(len(nums)):
    nums_ = nums.copy()
    nums_.pop(i)
    for j in range(len(nums_)):
        nums__ = nums_.copy()
        nums__.pop(j)
        diff = S - sum(nums__)
        if best_diff == None or abs(diff) < best_diff:
            best_diff = abs(diff)
            # best_nums = [nums[i], nums_[j]]

print(best_diff)


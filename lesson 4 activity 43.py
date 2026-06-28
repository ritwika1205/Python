nums = [2, -5, 3, 4, -1, 6, -3]
print("Full array:", nums)
print()
print("Some subarrays:")
print("[0:2] ->", nums[0:2], "sum =", sum(nums[0:2]))   # [2, -5]
print("[2:6] ->", nums[2:6], "sum =", sum(nums[2:6]))   # [3, 4, -1, 6]
print("[3:7] ->", nums[3:7], "sum =", sum(nums[3:7]))   # [4, -1, 6, -3]
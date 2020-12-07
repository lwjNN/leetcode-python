"""
快排
"""
from typing import List


def quickSort(nums: List):
    if not nums or len(nums) == 1:
        return nums
    mid = nums[len(nums) // 2]
    left, right = [], []
    nums.remove(mid)
    for num in nums:
        if num > mid:
            right.append(num)
        else:
            left.append(num)
    return quickSort(left) + [mid] + quickSort(right)


print(quickSort([9,1,8,3,4,7,6,5]))

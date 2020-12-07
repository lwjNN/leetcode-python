from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, len(nums)-1
    res = 0
    while left < right:
        if nums[left] + nums[right] < k:
            left += 1
        elif nums[left] + nums[right] > k:
            right -= 1
        else:
            res += 1
            left += 1
            right -= 1
    return res
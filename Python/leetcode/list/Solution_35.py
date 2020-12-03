from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    r = len(nums)
    l= 0
    while l <= r:
        mid = (r + l) // 2
        if mid > len(nums) -1:
            return len(nums)
        if nums[mid] > target:
            r = mid-1
        elif nums[mid] < target:
            l = mid+1
        else:
            return mid
    return l


print(searchInsert([1,3,5,6], 8))

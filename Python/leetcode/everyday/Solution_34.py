from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    res = []
    len = len(nums)
    start, end = 0, len-1

    while start < end:
        mid = (end - start) // 2
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            start = mid // 2
            end
    return res

print(searchRange([1,2,2,2], 4))

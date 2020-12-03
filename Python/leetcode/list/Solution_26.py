from typing import List


def removeDuplicates(nums: List[int]) -> int:
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1
    return count


l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(l))

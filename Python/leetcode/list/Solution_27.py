from typing import List


def removeElement(nums: List[int], val: int) -> int:
    count = 0
    for num in nums:
        if num != val:
            nums[count] = num
            count += 1
    return count


def removeElement_1(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)

    print(nums)
    return len(nums)

l = [3,2,2,3,0,1,4]
print(removeElement_1(l, 3))

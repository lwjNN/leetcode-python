from typing import List


def waysToMakeFair(nums: List[int]) -> int:
    count = 0
    a = sum(nums[::2])#奇数和
    b = sum(nums[1::2])#偶数和
    for i in range(len(nums)):
        if i % 2 == 0:
            js = a - nums[i]#以后的偶数和




print(waysToMakeFair([2, 1, 6, 4]))

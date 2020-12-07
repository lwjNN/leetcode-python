"""
冒泡排序
"""
from typing import List


def BubbleSort(nums: List):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if (nums[j] > nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

print(BubbleSort([7,4,6,3,5,2,1]))

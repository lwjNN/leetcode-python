"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroCount = 0
    for i in nums:
        if i == 0:
            zeroCount += 1
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(zeroCount):
        nums[len(nums) - zeroCount + i] = 0
    print(nums)


moveZeroes([0, 1, 0, 3, 12])


def moveZeroes_2(nums: List[int]) -> None:
    if not nums:
        return None
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j], nums[i] = nums[j], nums[j]
            j += 1
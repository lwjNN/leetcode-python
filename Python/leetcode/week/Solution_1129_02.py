from typing import List


def mostCompetitive(nums: List[int], k: int) -> List[int]:
    result = []
    minEle = min(nums[:len(nums) - k + 1])
    index = nums.index(minEle)
    result.append(minEle)
    m = 1
    for i in range(index,index + k-1):
        ele = min(nums[index + 1: len(nums) - k + 1 + m])
        index = nums.index(ele,index + 1)
        result.append(ele)
        m += 1
    return result


print(mostCompetitive([2,4,3,3,5,4,9,6], 4))

from typing import List


def minimumIncompatibility(nums: List[int], k: int) -> int:
    l = len(nums)
    if l == 1:
        return 1
    nums.sort()
    res = 0
    d = []
    b = [False] * l
    for i in range(l):
        b[i] = True
        for j in range(i, l):
            if not b[j]:
                if j == i:
                    continue
                else:
                    res += nums[j] - nums[i]
                    b[j] = True
    return res

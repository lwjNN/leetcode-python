from typing import List


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [nums[0]]
    res = dp[0]
    for i in range(1, len(nums)):
        if dp[i - 1] > 0:
            dp.append(dp[i - 1] + nums[i])
        else:
            dp.append(nums[i])

    for i in range(1, len(dp)):
        res = max(res, dp[i])
    print(dp)
    return res

l = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(l))

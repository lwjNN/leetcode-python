from _ast import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 从第三个元素开始遍历
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]);
        return dp[len(nums)-1]

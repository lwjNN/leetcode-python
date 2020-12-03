from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        nums1 = nums[1:]
        nums2 = nums[:len(nums)-1]
        return max(self.rob_dp(nums1), self.rob_dp(nums2))

    def rob_dp(self,nums):
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
        return dp[len(nums) - 1]


a = [1,2,3,1]
print(Solution().rob(a))
from _ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(i,tmp):
            ans.append(tmp)
            for j in range(i, n):
                backtrack(j+1,tmp + [nums[j]])

        backtrack(0, [])
        return ans

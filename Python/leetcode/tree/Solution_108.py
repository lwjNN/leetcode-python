from _ast import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(nums: List[int], left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode(nums[mid])
            root.left = buildTree(nums, left, mid - 1)
            root.right = buildTree(nums, mid + 1, right)
            return root

        return buildTree(nums, 0, len(nums) - 1)

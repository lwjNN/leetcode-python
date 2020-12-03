# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from _ast import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(lists: List[int]) -> TreeNode:
            lengh = len(lists)
            if lengh == 0:
                return
            root = TreeNode(nums[lengh/2])
            root.left = buildTree(lists[:lengh//2])
            root.right = buildTree(lists[lengh//2 + 1:])
            return root
        return buildTree(nums)

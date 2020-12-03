# Definition for a binary tree node.
from _ast import List


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        tmp = []
        def helper(node: TreeNode, tar, tmp = []):
            if not node:
                return
            tmp.append(node.val)
            if not node.left and not node.right and tar == node.val:
                ans.append(tmp)
            helper(node.left, tar - node.val, tmp)
            helper(node.right, tar - node.val, tmp)
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode, lower, upper) -> bool:
            if not node:
                return True
            val = node.val
            if not lower and lower >= val:
                return False
            if not upper and upper <= val:
                return False
            if not dfs(node.left,lower, val):
                return False
            if not dfs(node.right, val,upper):
                return False
            return True

        return dfs(root, None, None)


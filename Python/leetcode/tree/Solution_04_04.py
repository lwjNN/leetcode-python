# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def getMaxDepth(node: TreeNode) -> int:
            if not node:
                return 0
            return max(getMaxDepth(node.left),getMaxDepth(node.right)) + 1

        return abs(getMaxDepth(root.left) - getMaxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def _isSymmetric(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return _isSymmetric(left.left, right.right) and _isSymmetric(left.right, right.left)

        return _isSymmetric(root.left, root.right)

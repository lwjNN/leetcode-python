class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True

    def height(node: TreeNode) -> int:
        if not node:
            return 0

        leftHeight = height(node.left)
        rightHeight = height(node.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    return height(root) >= 0


class Solution:
    pass

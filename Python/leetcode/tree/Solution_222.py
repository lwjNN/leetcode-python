class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def countNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    lCount = countNodes(root.left)
    rCount = countNodes(root.right)
    if lCount == 0 and rCount == 0:
        return 1
    else:
        return lCount + rCount

from _ast import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if not root:
            return paths

        def helper(node: TreeNode, path):
            if node:
                path += str(root.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    helper(node.left, path)
                    helper(node.right, path)

        helper(root, "")
        return paths
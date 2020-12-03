class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children or len(root.children) == 0:
            return 1
        list = []
        for node in root.children:
            list.append(self.maxDepth(node))
        return max(list) + 1

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                next = cur.left
                preNode = next
                while preNode.right:
                    preNode = preNode.right
                preNode.right = cur.right
                cur.left = None
                cur.right = next
            cur = cur.right

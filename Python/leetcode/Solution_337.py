
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    dict = dict()
    def rob_recursion(self, root: TreeNode) -> int:
        if not root:
            return 0
        monet = root.val
        if root.left:
            monet += (self.rob_recursion(root.left.left) + self.rob_recursion(root.left.right))
        if root.right:
            monet += (self.rob_recursion(root.right.left) + self.rob_recursion(root.right.right))
        return max(monet, self.rob_recursion(root.left) + self.rob_recursion(root.right))


    def rob_hashdp(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in dict:
            return dict.get(root)
        money = root.val
        if root.left:
            money += (self.rob_hashdp(root.left.left) + self.rob_hashdp(root.left.right))
        if root.right:
            money += (self.rob_hashdp(root.right.left) + self.rob_hashdp(root.right.right))
        result = max(money, self.rob_hashdp(root.left) + self.rob_hashdp(root.right))
        dict[root] = result
        return result
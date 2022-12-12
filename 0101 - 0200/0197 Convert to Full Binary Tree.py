# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if not root: return None
        if ((root.left is not None) + (root.right is not None)) == 1: return None

        root.left = self.solve(root.left)
        root.right = self.solve(root.right)

        return root

    def solve(self, root):
        while root and ((root.left is not None) + (root.right is not None)) == 1: root = root.left if root.left else root.right
        return self.helper(root)

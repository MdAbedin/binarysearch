# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root:
            root.left, root.right = self.solve(root.right), self.solve(root.left)
            return root

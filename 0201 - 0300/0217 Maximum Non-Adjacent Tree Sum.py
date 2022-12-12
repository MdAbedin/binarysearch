# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, usable=True):
        if not root:
            return 0

        if usable:
            return max(root.val + self.solve(root.left, False) + self.solve(root.right, False), self.solve(root.left, True) + self.solve(root.right, True))
        else:
            return self.solve(root.left, True) + self.solve(root.right, True)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return None

        left = self.solve(root.left)
        right = self.solve(root.right)

        if not left and not right and root.val % 2 == 0: return None

        root.left = left
        root.right = right

        return root

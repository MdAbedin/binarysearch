# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        return not root0 and not root1 if not root0 or not root1 else root0.val == root1.val and ((self.solve(root0.left,root1.left) and self.solve(root0.right,root1.right)) or (self.solve(root0.left,root1.right) and self.solve(root0.right,root1.left)))

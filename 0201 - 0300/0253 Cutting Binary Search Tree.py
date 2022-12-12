# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, lo, hi):
        if not root: return None
        if not (lo <= root.val <= hi): return self.solve(root.left,lo,hi) if self.solve(root.left,lo,hi) else self.solve(root.right,lo,hi)

        root.left, root.right = self.solve(root.left,lo,hi), self.solve(root.right,lo,hi)
        return root

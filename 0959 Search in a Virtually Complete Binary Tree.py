# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if not root: return False
        if root.val == target: return True
        return self.solve(root.left,target) or self.solve(root.right, target)

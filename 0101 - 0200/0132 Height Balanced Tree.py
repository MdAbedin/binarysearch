# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, start=True):
        if not root:
            return True if start else 0

        x,y = self.solve(root.left,False),self.solve(root.right,False)

        if type(x)==bool:return x
        if type(y)==bool:return y
        if abs(x-y) > 1: return False

        return True if start else max(x,y)+1

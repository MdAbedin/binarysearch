# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root,start=True):
        if not root:
            return True if start else [inf,-inf]

        x = self.solve(root.left,False)
        y = self.solve(root.right,False)

        if type(x) == bool:
            return x
        if type(y) == bool:
            return y

        a,b=x
        c,d=y

        if b >= root.val: return False
        if c <= root.val: return False

        return True if start else [min(a,root.val),max(d,root.val)]

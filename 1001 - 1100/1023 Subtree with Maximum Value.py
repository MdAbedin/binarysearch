# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root,start=1):
        if not root: return 0,0

        l,r = self.solve(root.left,0),self.solve(root.right,0)
        a,b = l[0]+r[0]+root.val,max(l[0]+r[0]+root.val,max(l[1],r[1]))
        
        if start == 1:
            return b
        else:
            return a,b

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if not root: return 0,0

        l = self.helper(root.left)
        r = self.helper(root.right)

        return max(l[0],r[0],1+l[1]+r[1]), 1+max(l[1],r[1])

    def solve(self, root):
        return self.helper(root)[0]

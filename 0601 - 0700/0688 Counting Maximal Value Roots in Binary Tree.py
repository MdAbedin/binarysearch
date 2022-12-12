# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root: return 0,-inf

        l,r = self.helper(root.left), self.helper(root.right)

        return l[0]+r[0]+(1 if root.val >= max(l[1], r[1]) else 0), max(root.val,l[1],r[1])

    def solve(self, root):
        return self.helper(root)[0]

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, values, first = True):
        if first:
            values = set(values)

        if not root:
            return 0

        l,r = self.solve(root.left, values, False), self.solve(root.right, values, False)

        if type(l) != int:
            return l
        if type(r) != int:
            return r
        
        found = l + r + (root.val in values)

        return root if found == len(values) else found

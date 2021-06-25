# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, use=0):
        if not root:
            return 0

        ans = use*root.val
        use2 = 1 if root.val%2 == 0 else 0
        
        if root.left:
            if root.left.left:
                ans += root.left.left.val*use2

            if root.left.right:
                ans += root.left.right.val*use2

        if root.right:
            if root.right.left:
                ans += root.right.left.val*use2

            if root.right.right:
                ans += root.right.right.val*use2

        return ans + self.solve(root.left,0) + self.solve(root.right,0)

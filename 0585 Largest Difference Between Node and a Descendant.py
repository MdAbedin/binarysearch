# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root or (not root.left and not root.right):
            return 0

        ans = 0

        def helper(node):
            nonlocal ans

            if not node:
                return None,None

            max_l,min_l = helper(node.left)
            max_r,min_r = helper(node.right)
            max_cur, min_cur = node.val, node.val

            if max_l is not None:
                ans = max(ans, abs(node.val - max_l))
                ans = max(ans, abs(node.val - min_l))
                max_cur = max(max_cur, max_l)
                min_cur = min(min_cur, min_l)

            if max_r is not None:
                ans = max(ans, abs(node.val - max_r))
                ans = max(ans, abs(node.val - min_r))                
                max_cur = max(max_cur, max_r)
                min_cur = min(min_cur, min_r)

            return max_cur, min_cur

        helper(root)

        return ans

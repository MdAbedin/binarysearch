# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def helper(root):
            if not root: return 1, 0
            if not root.left and not root.right: return 1, 1
            
            l_ans, l_size = helper(root.left)
            r_ans, r_size = helper(root.right)
            root_size = l_size + r_size + 1
            
            if root.left and root.right:
                return l_ans * r_ans * comb(l_size + r_size, l_size), root_size
            elif root.left:
                return l_ans, root_size
            else:
                return r_ans, root_size

        return helper(root)[0]

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, start=True):
        if not root:
            return 0,None

        ln,lv = self.solve(root.left,False)
        rn,rv = self.solve(root.right,False)
        
        is_unival = (lv == root.val or lv is None) and (rv == root.val or rv is None)
        ans_n = ln + rn + is_unival
        ans_v = root.val if is_unival else "not unival"
        
        return ans_n if start else (ans_n, ans_v)

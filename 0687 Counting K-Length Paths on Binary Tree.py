# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k, start = True):
        if not root: return {0:1}, 0

        l_counts, l_ans = self.solve(root.left, k, False)
        r_counts, r_ans = self.solve(root.right, k, False)

        cur_counts, cur_ans = {0:1,1:1}, l_ans + r_ans

        for length in range(k):
            if length > 1: cur_counts[length] = l_counts.get(length-1, 0) + r_counts.get(length-1, 0)
            cur_ans += l_counts.get(length, 0) * r_counts.get(k-length-1, 0)

        return cur_ans if start else (cur_counts, cur_ans)

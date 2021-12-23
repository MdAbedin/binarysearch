# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def sum_count_max_avg(root):
            if not root: return 0,0,0

            l_sum,l_count,l_max_avg = sum_count_max_avg(root.left)
            r_sum,r_count,r_max_avg = sum_count_max_avg(root.right)

            total_sum = l_sum+r_sum+root.val
            total_count = l_count+r_count+1
            total_max_avg = max(l_max_avg,r_max_avg,total_sum/total_count)

            return total_sum,total_count,total_max_avg

        return sum_count_max_avg(root)[2]

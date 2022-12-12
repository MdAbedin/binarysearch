# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, start=True):
        if not root:
            return None if start else [{},0]

        counts = defaultdict(int)
        lcounts,lsum = self.solve(root.left,False)
        rcounts,rsum = self.solve(root.right,False)
        cur_sum = lsum+rsum+root.val

        for sum_,count in list(lcounts.items()) + list(rcounts.items()):
            counts[sum_] += count

        counts[cur_sum] += 1

        return max(counts, key = lambda x: counts[x]) if start else [counts, cur_sum]

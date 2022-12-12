# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        self.k_counts = 0

        def path_sum_counts(node):
            if not node: return {}

            l,r = path_sum_counts(node.left), path_sum_counts(node.right)
            ans = defaultdict(int)

            for path_sum,count in list(l.items()) + list(r.items()):
                ans[path_sum + node.val] += count

            ans[node.val] += 1
            self.k_counts += ans[k]

            return ans

        path_sum_counts(root)

        return self.k_counts

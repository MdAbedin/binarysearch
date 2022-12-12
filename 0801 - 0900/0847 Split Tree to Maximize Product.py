# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        sums = dict()

        def get_sums(root):
            if not root:
                return 0

            sums[root] = root.val + get_sums(root.left) + get_sums(root.right)
            
            return sums[root]

        total = get_sums(root)
        dfs = [root]
        ans = 0

        while dfs:
            cur = dfs.pop()

            if cur.left:
                ans = max(ans, sums[cur.left]*(total-sums[cur.left]))
                dfs.append(cur.left)

            if cur.right:
                ans = max(ans, sums[cur.right]*(total-sums[cur.right]))
                dfs.append(cur.right)

        return ans

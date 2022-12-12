# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        ans = []

        dfs = [[root,0]]

        while dfs:
            cur,i = dfs.pop()

            if i >= len(ans): ans.append(0)
            ans[i] += cur.val

            if cur.left: dfs.append([cur.left,i+1])
            if cur.right: dfs.append([cur.right,i])

        return ans

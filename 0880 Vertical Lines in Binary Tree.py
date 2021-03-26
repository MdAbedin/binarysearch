# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        ans = set()
        dfs = [[root,0]]

        while dfs:
            cur,x = dfs.pop()
            ans.add(x)

            if cur.left: dfs.append([cur.left,x-1])
            if cur.right: dfs.append([cur.right,x+1])

        return len(ans)

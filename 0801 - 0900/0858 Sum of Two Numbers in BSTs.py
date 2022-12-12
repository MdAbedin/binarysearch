# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, a, b, target):
        a_nums = set()
        dfs = [a]
        while dfs:
            cur = dfs.pop()
            a_nums.add(cur.val)

            if cur.left:dfs.append(cur.left)
            if cur.right:dfs.append(cur.right)

        dfs = [b]
        while dfs:
            cur = dfs.pop()
            if target-cur.val in a_nums:return True
            if cur.left:dfs.append(cur.left)
            if cur.right:dfs.append(cur.right)

        return False

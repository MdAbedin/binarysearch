# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,target):
        if not root or not target: return root == target == None
        return root.val == target.val and self.helper(root.left,target.left) and self.helper(root.right, target.right)

    def solve(self, root, target):
        dfs = [root]

        while dfs:
            cur = dfs.pop()
            if self.helper(cur,target): return True
            if cur.left: dfs.append(cur.left)
            if cur.right: dfs.append(cur.right)

        return False

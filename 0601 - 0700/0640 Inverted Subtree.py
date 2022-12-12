# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_inversion(self, source, target):
        if not source and not target: return True
        if not source or not target: return False

        return source.val == target.val and ((self.is_inversion(source.left,target.left) and self.is_inversion(source.right,target.right)) or (self.is_inversion(source.left,target.right) and self.is_inversion(source.right,target.left)))

    def solve(self, source, target):
        dfs = [target]
        target_nodes = []
        
        while dfs:
            cur = dfs.pop()
            target_nodes.append(cur)
            if cur.left: dfs.append(cur.left)
            if cur.right: dfs.append(cur.right)

        return any(self.is_inversion(source,target_node) for target_node in target_nodes)

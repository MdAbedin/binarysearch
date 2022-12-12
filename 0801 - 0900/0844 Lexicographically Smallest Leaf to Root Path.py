# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return []

        self.ans = deque([10])

        def helper(node, path):
            if not node: return

            path.appendleft(node.val)
            
            if not node.left and not node.right:
                if path < self.ans: self.ans = copy.copy(path)
            else:
                helper(node.left,path)
                helper(node.right,path)
            
            path.popleft()

        helper(root,deque())

        return list(self.ans)

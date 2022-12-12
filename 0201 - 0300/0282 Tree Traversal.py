# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        dfs = [[root,None]]

        while dfs:
            cur,parent = dfs.pop()
            cur.parent = parent

            if cur.left: dfs.append([cur.left,cur])
            if cur.right: dfs.append([cur.right,cur])
        
        cur = root

        for move in moves:
            if move == "RIGHT":
                cur = cur.right
            elif move == "LEFT":
                cur = cur.left
            else:
                cur = cur.parent

        return cur.val

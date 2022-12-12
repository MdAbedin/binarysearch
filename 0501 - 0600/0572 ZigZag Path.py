# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, last=None, total=0):
        if not root:
            return total

        if last is None:
            return max(self.solve(root.left,"left",total+1), self.solve(root.right,"right",total+1))
        elif last == "left":
            return max(self.solve(root.right,"right", total+1), self.solve(root.left, "left", 1))
        else:
            return max(self.solve(root.left,"left", total+1), self.solve(root.right, "right", 1))

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        ans = 0

        while node:
            ans *= 2
            ans += node.val
            node = node.next

        return ans

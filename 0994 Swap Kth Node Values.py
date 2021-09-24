# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        l = 0
        c = node
        while c:
            c = c.next
            l += 1
        c1 = node
        x = k
        while x:
            c1 = c1.next
            x -= 1

        x = l-k-1
        c2 = node
        while x:
            c2 = c2.next
            x -= 1

        c1.val,c2.val = c2.val,c1.val
        return node

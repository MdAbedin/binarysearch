# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        slow,fast = node, node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next

        return slow.val

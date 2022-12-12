# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        head = node

        while node and node.next:
            later = node.next.next
            node.val, node.next.val = node.next.val, node.val
            node = later

        return head

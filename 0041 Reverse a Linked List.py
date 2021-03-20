# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        prev = None

        while node:
            temp = node.next
            node.next = prev

            prev = node
            node = temp
            
        return prev

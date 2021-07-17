# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        if not node: return None

        head = node
        delete_prev = None
        delete = None
        prev = None
        
        while node:
            if node.val == target:
                delete = node
                delete_prev = prev
            prev = node
            node = node.next

        if delete == head: return head.next
        if not delete: return head

        delete_prev.next = delete.next
        return head

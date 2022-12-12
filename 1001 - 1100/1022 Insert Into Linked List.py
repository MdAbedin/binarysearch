# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):
        if pos == 0:
            new = LLNode(val)
            new.next = head
            return new

        cur = head
        while pos-1:
            cur = cur.next
            pos -= 1
        new = LLNode(val)
        new.next = cur.next
        cur.next = new

        return head

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node,count):
        old_head = node

        prev,cur = None,node

        for i in range(count):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        old_head.next = cur

        return prev

    def solve(self, node, i, j):
        if not node: return None
        if not node.next: return node
        if j==i: return node
        if i == 0: return self.reverse(node,j-i+1)

        ans_head = node
        prev,cur = None,node

        for x in range(i):
            prev = cur
            cur = cur.next

        prev.next = self.reverse(cur,j-i+1)

        return ans_head

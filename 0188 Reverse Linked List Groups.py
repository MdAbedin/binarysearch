# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        nodes = []
        while node:
          nodes.append(node.val)
          node = node.next
          
        ans = []
        for i in range(0,len(nodes),k):
          ans += nodes[i:i+k][::-1]
          
        head = LLNode(0)
        cur = head
        
        for val in ans:
          cur.next = LLNode(val)
          cur = cur.next
          
        return head.next

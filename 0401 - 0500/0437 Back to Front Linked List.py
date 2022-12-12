# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        nodes_list = []
        
        while node:
            nodes_list.append(node)
            node = node.next

        ans_head = LLNode(None)
        cur = ans_head

        for i in range(len(nodes_list)):
            cur.next = nodes_list[-i//2-1 if i%2 == 0 else i//2]
            cur = cur.next

        cur.next = None
            
        return ans_head.next

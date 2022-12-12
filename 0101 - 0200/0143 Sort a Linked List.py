# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if not node: return None
        
        nums = []

        while node:
            nums.append(node.val)
            node = node.next

        nums.sort()
        nodes = [LLNode(num) for num in nums]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        return nodes[0]

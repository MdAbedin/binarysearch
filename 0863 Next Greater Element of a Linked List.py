# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    
class Solution:
    def solve(self, node):
        unmatched = []
        head = node

        while node:
            while unmatched and unmatched[0].priority < node.val:
                heappop(unmatched).item.val = node.val

            heappush(unmatched, PrioritizedItem(node.val, node))
            node = node.next

        while unmatched:
            heappop(unmatched).item.val = 0

        return head

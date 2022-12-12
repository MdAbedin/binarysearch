class Solution:
    def solve(self, pushes, pops):
        stack = []
        queue = deque(pops)

        for num in pushes:
            stack.append(num)

            while queue and stack and queue[0] == stack[-1]:
                stack.pop()
                queue.popleft()

        return not stack and not queue

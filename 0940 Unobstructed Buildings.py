class Solution:
    def solve(self, heights):
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack

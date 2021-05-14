class Solution:
    def solve(self, s):
        stack = []

        for c in s:
            if stack and stack[-1][0] != c and stack[-1][1] > 1:
                stack.pop()

            if not stack or c != stack[-1][0]:
                stack.append([c,1])
            else:
                stack[-1][1] += 1

        if stack and stack[-1][1] > 1:
            stack.pop()

        return "".join(e[0] for e in stack)

class Solution:
    def solve(self, nums):
        stack = []
        turns = 0

        for num in nums:
            if stack and stack[-1] == num:
                stack.pop()
                turns += 1
            else:
                stack.append(num)

        return turns%2 == 1

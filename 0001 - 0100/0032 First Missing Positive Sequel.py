class Solution:
    def solve(self, arr):
        expecting = 1

        for num in arr:
            if num > expecting:
                return expecting
            elif num == expecting:
                expecting += 1

        return expecting

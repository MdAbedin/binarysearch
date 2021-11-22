class Solution:
    def solve(self, lst):
        nums_to_right = []
        ans = []

        for num in reversed(lst):
            ans.append(bisect_left(nums_to_right, num))
            insort(nums_to_right, num)

        ans.reverse()

        return ans

class Solution:
    def solve(self, nums):
        total_sum = sum(nums)
        if total_sum%2 == 1: return False

        possible_sums = [True] + [False]*(total_sum//2)

        for num in nums:
            new_possible_sums = copy.copy(possible_sums)

            for sum_ in range(num,len(new_possible_sums)):
                if possible_sums[sum_-num]:
                    new_possible_sums[sum_] = True

            possible_sums = new_possible_sums

        return possible_sums[total_sum//2]

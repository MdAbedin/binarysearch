class Solution:
    def solve(self, nums, k):
        counts = defaultdict(int)
        ans = []
        distincts = 0

        for i in range(len(nums)):
            if counts[nums[i]] == 0: distincts += 1
            counts[nums[i]] += 1

            if i >= k-1: ans.append(distincts)

            if i-k+1 >= 0:
                if counts[nums[i-k+1]] == 1: distincts -= 1
                counts[nums[i-k+1]] -= 1

        return ans

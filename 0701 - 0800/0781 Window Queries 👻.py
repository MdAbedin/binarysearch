class Solution:
    def solve(self, nums, queries, w):
        ans = defaultdict(int)
        furthests = defaultdict(lambda: w-2)

        for i,num in enumerate(nums):
            ans[num] += max(0,min(len(nums)-1, i + (w-1)) - max(i-1, furthests[num]))
            furthests[num] = i + (w-1)

        return [ans[q] for q in queries]

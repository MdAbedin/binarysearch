class Solution:
    def solve(self, nums, k):
        target = sum(1 if num > k else (-1 if num < k else 0) for num in nums)
        if target == 0: return len(nums)
        
        ans = inf
        psum = 0
        lasts = defaultdict(lambda: -inf, {0:-1})

        for i,num in enumerate(nums):
            if num > k: psum += 1
            if num < k: psum -= 1

            ans = min(ans, i - lasts[psum - target])

            lasts[psum] = i

        return len(nums) - ans

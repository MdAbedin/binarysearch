class Solution:
    def solve(self, nums, target):
        ans = None
        ans_diff = inf
        l,r = min(min(nums),floor(target/len(nums))),max(nums)

        while l <= r:
            m = (l+r)//2

            new_sum = sum(min(num,m) for num in nums)
            diff = abs(new_sum - target)
            
            if diff < ans_diff or (diff == ans_diff and m < ans):
                ans = m
                ans_diff = diff

            if new_sum < target:
                l = m+1
            else:
                r = m-1

        return ans

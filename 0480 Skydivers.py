class Solution:
    def solve(self, nums, k):
        def works(cap):
            days_used = 1
            cap_left = cap

            for num in nums:
                if num <= cap_left:
                    cap_left -= num
                else:
                    cap_left = cap-num
                    days_used += 1

            return days_used <= k

        if not nums:
            return 0

        l,r = max(nums),sum(nums)
        ans = -1

        while l <= r:
            mid = (l+r)//2

            if works(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans

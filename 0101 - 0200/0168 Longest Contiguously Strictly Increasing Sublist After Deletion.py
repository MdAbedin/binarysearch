class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        l = [1]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                l.append(l[-1]+1)
            else:
                l.append(1)

        r = [1]

        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                r.append(r[-1]+1)
            else:
                r.append(1)

        r.reverse()
        ans = max(max(r), max(l))

        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i+1]:
                ans = max(ans, l[i-1]+r[i+1])

        return ans

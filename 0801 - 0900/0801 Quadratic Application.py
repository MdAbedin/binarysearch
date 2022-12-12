class Solution:
    def solve(self, nums, a, b, c):
        q = lambda x: a*(x**2)+b*x+c
        if not nums: return []
        if len(nums) == 1:
            return list(map(q,nums))
        if a == 0:
            if b > 0:
                return list(map(q,nums))
            else:
                return list(map(q,reversed(nums)))
            
        if a > 0:
            i = bisect_left(nums, -b/(2*a))
            j = i-1
        else:
            i = 0
            j = len(nums)-1

        ans = []

        while (i < len(nums) or j >= 0) and (a > 0 or i <= j):
            if i == len(nums):
                ans.append(q(nums[j]))
                j -= 1
            elif j == -1:
                ans.append(q(nums[i]))
                i += 1
            else:
                if q(nums[i]) < q(nums[j]):
                    ans.append(q(nums[i]))
                    i += 1
                else:
                    ans.append(q(nums[j]))
                    j -= 1

        return ans

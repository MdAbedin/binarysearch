class Solution:
    def solve(self, nums):
        has_zero = 0 in nums
        sublists = []
        sublist = []
        
        for num in nums:
            if num == 0:
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(num)

        sublists.append(sublist)

        ans = -inf

        for sublist in sublists:
            if not sublist: continue
            total = prod(sublist)
            for num in sublist:
                ans = max(ans, total)
                total //= num
            total = prod(sublist)
            for num in reversed(sublist):
                ans = max(ans, total)
                total //= num

        return max(ans, 0 if has_zero else -inf)

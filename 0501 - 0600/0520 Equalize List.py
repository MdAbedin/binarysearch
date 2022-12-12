class Solution:
    def solve(self, nums, costs):
        def cost(x):
            return sum(abs(num-x)*cost for num,cost in zip(nums,costs))
        
        l,r = min(nums),max(nums)
        ans = cost(l)

        while l<=r:
            m = (l+r)//2

            if cost(m) <= cost(m+1):
                if cost(m) < ans:
                    ans = cost(m)
                r = m-1
            else:
                l = m+1

        return ans

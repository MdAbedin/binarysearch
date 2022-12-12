class Solution:
    def __init__(self):
        factorials = [1]
        for i in range(1,16):
            factorials.append(factorials[-1]*i)
        self.factorials = factorials

    def helper(self,i,used,cur,nums):
        if i == len(nums)-1:
            return self.factorials[nums[i]-1-used]*cur

        ans = 0

        for j in range(nums[i]-used):
            ans += self.helper(i+1,used+j+1,cur*comb(nums[i]-used-1,j)*self.factorials[j],nums)

        return ans

    def solve(self, n, k):
        self.n = n
        ans = 0
        nums = list(range(1,n+1))

        for combo in combinations(nums,k):
            combo = sorted(list(combo))
            if combo[-1] != n: continue
            ans += self.helper(0,0,1,combo)

        return ans

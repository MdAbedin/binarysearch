class Solution:
    def solve(self, nums, operations):
        ans = [0]*(len(nums)+1)
        
        for l,r,x in operations:
            ans[l] += x
            ans[r+1] -= x

        for i in range(1,len(ans)):
            ans[i] += ans[i-1]

        return [num + add for num,add in zip(nums,ans)]

class Solution:
    def solve(self, nums):
        if not nums: return 0
        
        mx = ceil(log(max(max(nums),1)*2,2))+1
        counts = Counter(nums)
        ans = 0

        for i in range(mx+1):
            s = 2**i
            for num in counts:
                if num == max(num, s-num):
                    if s-num == num:
                        ans += (counts[num]*(counts[num]-1))//2
                    else:
                        ans += (counts[num]*(counts[s-num]))

        return ans                    

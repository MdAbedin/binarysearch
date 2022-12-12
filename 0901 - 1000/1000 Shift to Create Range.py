class Solution:
    def solve(self, nums):
        if 1 not in nums: return False

        i = nums.index(1)
        inc = True
        
        for j in range(i,i+len(nums)-1):
            j %= len(nums)
            nxt = (j+1)%len(nums)
            if nums[nxt] != nums[j]+1:
                inc = False
                break

        if inc: return True

        if len(nums) not in nums: return False
        i = nums.index(len(nums))
        dec = True

        for j in range(i,i+len(nums)-1):
            j %= len(nums)
            nxt = (j+1)%len(nums)
            if nums[nxt] != nums[j]-1:
                return False
                
        return True

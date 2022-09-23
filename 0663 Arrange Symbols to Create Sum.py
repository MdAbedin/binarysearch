class Solution:
    def solve(self, nums, target):
        if not nums: return int(target == 0)
        
        sum_counts1 = Counter(sum(num if sign == "+" else -num for sign,num in zip(signs,nums[:len(nums)//2])) for signs in product("+-",repeat = len(nums)//2))
        sum_counts2 = Counter(sum(num if sign == "+" else -num for sign,num in zip(signs,nums[len(nums)//2:])) for signs in product("+-",repeat = len(nums) - len(nums)//2))
        
        return sum(count * sum_counts2.get(target - sum_, 0) for sum_, count in sum_counts1.items())

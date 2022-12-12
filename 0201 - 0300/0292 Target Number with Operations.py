class Solution:
    def solve(self, start, end):
        if start == 0: return 1 + solve(1,end)

        power = floor(log(end/start,2))
        diff = end - start*(2**power)
        ans = power
        
        for i in range(power,-1,-1):
            adds = diff//(2**i)
            ans += adds
            diff -= adds*(2**i)

            if diff == 0: break

        return ans
            

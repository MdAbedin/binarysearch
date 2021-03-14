class Solution:
    def solve(self, height, blacklist):
        blacklist = set(blacklist)
        if height in blacklist: return 0

        dp = [[0,1]]
        MOD = int(1e9+7)

        for i in range(1,height+1):
            if height-i in blacklist:
                dp.append([0,0])
                continue
            
            ans0,ans1 = 0,0

            ans0 += dp[i-1][1] if i-1>=0 else 0
            ans0 += dp[i-2][1] if i-2>=0 else 0
            ans0 += dp[i-4][1] if i-4>=0 else 0
            ans0 %= MOD

            ans1 += dp[i-1][0] if i-1>=0 else 0
            ans1 += dp[i-3][0] if i-3>=0 else 0
            ans1 += dp[i-4][0] if i-4>=0 else 0
            ans1 %= MOD
            
            dp.append([ans0,ans1])
        
        # print(dp)

        return sum(dp[-1])%MOD

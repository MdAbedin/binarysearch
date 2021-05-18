class Solution:
    def solve(self, s):
        l_streaks = [0]
        for i in range(len(s)):
            if s[i] == "1":
                l_streaks.append(l_streaks[-1]+1)
            else:
                l_streaks.append(0)

        r_streaks = [0]
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                r_streaks.append(r_streaks[-1]+1)
            else:
                r_streaks.append(0)
        
        r_streaks.reverse()

        if "1" not in s:
            return 0

        first_1 = s.find("1")
        last_1 = s.rfind("1")
        ans = max(s.find("0"), len(s)-1-s.rfind("0"))

        for i in range(len(s)):
            if s[i] == "0":
                if i-l_streaks[i] > first_1:
                    ans = max(ans, l_streaks[i]+r_streaks[i+1]+1)
                else:
                    if i+r_streaks[i+1] < last_1:
                        ans = max(ans, l_streaks[i]+r_streaks[i+1]+1)
                    else:
                        ans = max(ans, l_streaks[i]+r_streaks[i+1])

        return ans

class Solution:
    def solve(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] != "a" and not (i == len(s)//2 and len(s)%2==1):
                s[i] = "a"
                break
        else:
            s[-1] = "b"

        return "".join(s)

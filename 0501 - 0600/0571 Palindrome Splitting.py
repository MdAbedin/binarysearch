class Solution:
    def solve(self, s):
        if not s:
            return 1

        ans = 0

        for i in range(2**(len(s)-1)):
            bitmask = bin(i)[2:].rjust(len(s)-1, '0')
            one_indexes = [-1] + [i for i in range(len(bitmask)) if bitmask[i]=='1'] + [len(bitmask)]
            ans += all(s[one_indexes[j]+1:one_indexes[j+1]+1]==s[one_indexes[j]+1:one_indexes[j+1]+1][::-1] for j in range(len(one_indexes)-1))

        return ans

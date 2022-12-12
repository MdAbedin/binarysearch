class Solution:
    def solve(self, s, shifts):
        ans = []
        shift_sum = 0

        for i in reversed(range(len(s))):
            shift_sum += shifts[i]
            ans.append(chr((ord(s[i])-ord('a') + shift_sum)%26 + ord('a')))

        return "".join(reversed(ans))

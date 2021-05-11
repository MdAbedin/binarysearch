class Solution:
    def solve(self, start, end):
        ans = []

        for bit in range(len(bin(end)[2:])):
            ans.append(start//(2**bit)%2 if end//(2**bit) == start//(2**bit) else 0)

        ans.reverse()

        return int("".join(map(str,ans)),2)

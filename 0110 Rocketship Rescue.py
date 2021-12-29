class Solution:
    def solve(self, weights, limit):
        weights.sort()
        i,j = 0,len(weights)-1
        ans = 0

        while i < j:
            if weights[j] + weights[i] <= limit:
                i += 1

            ans += 1
            j -= 1

        if i == j: ans += 1

        return ans

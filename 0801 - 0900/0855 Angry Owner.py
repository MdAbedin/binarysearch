class Solution:
    def solve(self, customers, mood, k):
        deltas = [0]+[c if m == 0 else 0 for c,m in zip(customers,mood)]
        S = sum(c for c,m in zip(customers, mood) if m == 1)

        for i in range(1,len(deltas)):
            deltas[i] += deltas[i-1]

        return max(deltas[i]-deltas[i-k]+S for i in range(k,len(deltas)))

class Solution:
    def solve(self, s, k):
        if k > len(s):
            return False

        if k == 0:
            return s == ""

        odds = sum(x%2 == 1 for x in Counter(s).values())
        non_odds = len(s)-odds

        if odds > k:
            return False

        k -= odds

        if k%2 == 1:
            return non_odds >= k+1
        else:
            return non_odds >= k

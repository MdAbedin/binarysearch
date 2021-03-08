class Solution:
    def solve(self, dictionary, s):
        idxs = {dictionary[i]: i for i in range(len(dictionary))}
        mn = inf

        for i in range(len(s)-1,-1,-1):
            if s[i] not in idxs: continue

            mn = min(mn, idxs[s[i]])

            if idxs[s[i]] > mn: return False

        return True

class Solution:
    def solve(self, a, b):
        if Counter(a) != Counter(b): return []

        counts = defaultdict(int)
        diffs = 0
        ans = [0]

        for i in range(len(a)):
            counts[a[i]] += 1
            if counts[a[i]] == 1: diffs += 1

            counts[b[i]] -= 1
            if b[i] != a[i] and counts[b[i]] == -1: diffs += 1
            
            if counts[a[i]] == 0: diffs -= 1
            if b[i] != a[i] and counts[b[i]] == 0: diffs -= 1

            if diffs == 0: ans.append(i+1)

        ans.pop()
        
        return ans

class Solution:
    def solve(self, s):
        counts = defaultdict(list)

        for i in range(len(s)):
            for j in range(i,len(s)):
                counts["".join(sorted(s[i:j+1]))].append(s[i:j+1])

        return sorted([string for key in counts for string in counts[key] if len(counts[key])>1])

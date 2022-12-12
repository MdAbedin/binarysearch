class Solution:
    def solve(self, s0, s1):
        if len(s0) > len(s1): return 0
        if not s0 and not s1: return 0
        
        s0_counts = Counter(s0)
        counts = Counter(s1[:len(s0)])
        matches = sum(s0_counts[key] == counts[key] for key in s0_counts)
        s0_chars = len(set(s0))
        ans = 1 if matches == s0_chars else 0

        for i in range(1,len(s1)):
            if i+len(s0)-1 >= len(s1): break

            counts[s1[i-1]] -= 1
            if s1[i-1] in s0_counts and counts[s1[i-1]] != s0_counts[s1[i-1]]: matches -= 1
            if s1[i-1] in s0_counts and counts[s1[i-1]] == s0_counts[s1[i-1]]: matches += 1
            
            counts[s1[i+len(s0)-1]] += 1
            if s1[i+len(s0)-1] in s0_counts and counts[s1[i+len(s0)-1]] != s0_counts[s1[i+len(s0)-1]]: matches -= 1
            if s1[i+len(s0)-1] in s0_counts and counts[s1[i+len(s0)-1]] == s0_counts[s1[i+len(s0)-1]]: matches += 1

            if matches == s0_chars: ans += 1

        return ans

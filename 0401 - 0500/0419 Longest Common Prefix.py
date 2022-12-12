class Solution:
    def solve(self, words): return words[0][:next((i for i in range(min(len(word) for word in words)) if len(set(word[i] for word in words)) != 1),min(len(word) for word in words))]

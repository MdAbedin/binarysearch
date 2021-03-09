class Solution:
    def solve(self, text, word0, word1):
        words = text.split()
        if word0 not in words or word1 not in words: return -1

        last0, last1 = -inf,-inf
        ans = inf

        for i in range(len(words)):
            word = words[i]
            
            if word == word0:
                last0 = i
                ans = min(ans, i-last1-1)
            if word == word1:
                last1 = i
                ans = min(ans, i-last0-1)

        return ans

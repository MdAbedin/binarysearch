class Solution:
    def solve(self, words):
        words = sorted(list(set(words)), key = lambda x: len(x))
        words_set = set(words)
        ans = 0
        seen = set()

        for i,word in enumerate(words):
            if word in seen: continue
            
            seen.add(word)
            dfs = [[word,1]]

            while dfs:
                cur, streak = dfs.pop()
                ans = max(ans, streak)

                for char in ascii_lowercase:
                    if cur+char in words_set and cur+char not in seen:
                        seen.add(cur+char)
                        dfs.append([cur+char,streak+1])

        return ans

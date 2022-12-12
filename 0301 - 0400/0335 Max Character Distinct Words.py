class Solution:
    def solve(self, words):
        bitmasks = []

        for j,word in enumerate(words):
            bitmask = [0]*26
            distincts = 0

            for char in word:
                i = ord(char) - ord('a')
                if bitmask[i] == 0: distincts += 1
                bitmask[i] = 1
                if distincts == 26: break

            bitmasks.append(bitmask)

        ans = 0

        for i in range(len(words)):
            js = set(range(i+1,len(words)))

            for letter_i in range(26):
                if bitmasks[i][letter_i] == 0: continue

                for j in list(js):
                    if bitmasks[j][letter_i] == 1: js.remove(j)

            for j in js:
                ans = max(ans, len(words[i]) + len(words[j]))

        return ans

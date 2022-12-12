class Solution:
    def solve(self, words, letters):
        ans = 0
        counts = Counter(letters)

        for word in words:
            counts2 = deepcopy(counts)

            for letter in word:
                if counts2.get(letter,0) > 0:
                    counts2[letter] -= 1
                elif counts2.get("*",0) > 0:
                    counts2["*"] -= 1
                else:
                    break
            else:
                ans = max(ans,len(word))

        return ans

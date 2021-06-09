class Solution:
    def solve(self, words, s):
        locs = defaultdict(list)

        for i,char in enumerate(s):
            locs[char].append(i)

        def works(word):
            i = 0

            for char in word:
                j = bisect_left(locs[char], i)

                if j >= len(locs[char]):
                    return False

                i = locs[char][j]+1

            return True

        return sum(map(works, words))

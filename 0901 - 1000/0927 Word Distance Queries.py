class WordDistanceQuerier:
    def __init__(self, words):
        self.locs = defaultdict(list)
        
        for i,word in enumerate(words):
            self.locs[word].append(i)

    def distance(self, a, b):
        i,j = 0,0
        ans = inf

        while i < len(self.locs[a]) and j < len(self.locs[b]):
            if self.locs[a][i] == self.locs[b][j]:
                return 0

            while i < len(self.locs[a]) and self.locs[a][i] < self.locs[b][j]:
                ans = min(ans, self.locs[b][j]-self.locs[a][i])
                i += 1

            if i >= len(self.locs[a]):
                break

            while j < len(self.locs[b]) and self.locs[b][j] < self.locs[a][i]:
                ans = min(ans, self.locs[a][i]-self.locs[b][j])
                j += 1

        return ans

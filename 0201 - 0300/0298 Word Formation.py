class Solution:
    def solve(self, words, letters):
        counts = defaultdict(int,Counter(letters))
        lens = [len(word) for word in words if all(counts[char] >= count for char,count in Counter(word).items())]

        return max([0]+lens)

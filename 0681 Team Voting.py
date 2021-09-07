class Solution:
    def solve(self, votes):
        counts = defaultdict(lambda: [0]*26)
        
        for vote in votes:
            for i,char in enumerate(vote):
                counts[char][i] += 1

        def compare(char1, char2):
            for rank in range(26):
                if (diff := -(counts[char1][rank] - counts[char2][rank])) != 0:
                    return diff

            return ord(char1) - ord(char2)

        return "".join(sorted(counts.keys(), key = cmp_to_key(compare)))

class Solution:
    def solve(self, nums):
        freqs = sorted([list(pair) for pair in Counter(nums).most_common()],reverse=True)
        
        for i in range(1,len(freqs)):
          freqs[i][1] += freqs[i-1][1]

        return sum(freqs[i][1]*(freqs[i][0]-freqs[i+1][0]) for i in range(len(freqs)-1))

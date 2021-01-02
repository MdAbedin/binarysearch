class Solution:
    def solve(self, votes):
        votesd = dict()

        for i in range(len(votes)):
          if votes[i] < 0: votesd[i] = 0
          elif votes[i] >= len(votes): votesd[i] = 1
          elif i not in votesd:
            ppl = [i]
            while 0<=votes[ppl[-1]]<len(votes) and ppl[-1] not in votesd:
              ppl.append(votes[ppl[-1]])
            if votes[ppl[-1]] < 0: votesd[ppl[-1]] = 0
            elif votes[ppl[-1]] >= len(votes): votesd[ppl[-1]] = 1
            for p in  ppl:
              votesd[p] = votesd[ppl[-1]]
            
        return sum(v == 0 for v in votesd.values())

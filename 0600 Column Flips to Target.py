class Solution:
    def solve(self, matrix, target):
        counts1,counts2 = Counter(map(tuple,matrix)),Counter(map(tuple,target))

        key1 = next(iter(counts1))
        ans = inf

        for key2 in counts2:
            flips = [key1[i] != key2[i] for i in range(len(matrix[0]))]
            new_matrix = [[1-row[c] if flips[c] else row[c] for c in range(len(matrix[0]))] for row in matrix]
            
            if Counter(map(tuple,new_matrix)) == counts2:
                ans = min(ans, sum(flips))

        return -1 if ans == inf else ans

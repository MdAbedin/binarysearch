class Solution:
    def solve(self, matrix, k):
        return sorted(num for row in matrix for num in row)[k]

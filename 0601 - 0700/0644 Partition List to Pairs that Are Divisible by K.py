class Solution:
    def solve(self, nums, k):
        counts = Counter(num%k for num in nums)
        return all(counts[i]%2 == 0 if i == 0 or i == k-i else counts[i] == counts[k-i] for i in range(k))

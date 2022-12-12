class Solution:
    def solve(self, nums, k):
        MOD = 10**9+7
        pq = []
        ans = sum(nums)

        for num in nums:
            binary = list(bin(num)[2:][::-1])

            if "0" not in binary: binary.append("0")
            next_zero_i = binary.index("0")
            binary[next_zero_i] = "1"
            diff = 1 << next_zero_i

            heappush(pq, [diff, binary])

        for _ in range(k):
            diff, binary = heappop(pq)

            ans += diff
            ans %= MOD
            
            if "0" not in binary: binary.append("0")
            next_zero_i = binary.index("0")
            binary[next_zero_i] = "1"
            diff = 1 << next_zero_i

            heappush(pq, [diff, binary])

        return ans

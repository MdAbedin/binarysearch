class Solution:
    def solve(self, start, end):
        start_s, end_s = str(start), str(end)
        digits = "123456789"
        candidates = []

        for size in range(len(start_s), len(end_s)+1):
            candidates += [int(digits[i:i+size]) for i in range(len(digits)-size+1)]

        return [x for x in sorted(candidates) if start <= x <= end]

class Solution:
    def solve(self, nums):
        prev,prev2 = None,None
        lefts = []

        for num in nums:
            if num != prev: prev,prev2 = num,prev
            lefts.append(prev2)

        prev,prev2 = None,None
        rights = []

        for num in nums[::-1]:
            if num != prev: prev,prev2 = num,prev
            rights.append(prev2)

        rights.reverse()

        def is_peak(i):
            return (lefts[i] == None or lefts[i] < nums[i]) and \
                    (rights[i] == None or rights[i] < nums[i]) and \
                    ([lefts[i], rights[i]] != [None,None])

        return list(filter(is_peak, range(len(nums))))

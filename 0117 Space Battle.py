class Solution:
    def solve(self, nums):
        rights = []
        left_ans = []

        for num in nums:
            if num < 0:
                while rights and rights[-1] < abs(num):
                    rights.pop()

                if not rights:
                    left_ans.append(num)

                if rights and rights[-1] == abs(num):
                    rights.pop()
            else:
                rights.append(num)

        lefts = []
        right_ans = []

        for num in reversed(nums):
            if num > 0:
                while lefts and abs(lefts[-1]) < num:
                    lefts.pop()

                if not lefts:
                    right_ans.append(num)

                if lefts and abs(lefts[-1]) == num:
                    lefts.pop()
            else:
                lefts.append(num)

        right_ans = right_ans[::-1]
        
        return left_ans + right_ans

class Solution:
    def solve(self, nums):
        min_left_psum,max_left_psum = 0,0
        cur_psum = 0
        ans = 0

        for num in nums:
            cur_psum += num
            ans = max(ans, abs(cur_psum - min_left_psum), abs(cur_psum - max_left_psum))
            min_left_psum = min(min_left_psum, cur_psum)
            max_left_psum = max(max_left_psum, cur_psum)

        return ans

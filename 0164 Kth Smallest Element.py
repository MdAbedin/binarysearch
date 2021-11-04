class Solution:
    def solve(self, nums, k):
        def helper(l,r,rank):
            pivot_i = randint(l,r)
            nums[l],nums[pivot_i] = nums[pivot_i], nums[l]
            boundary_i = l+1

            for i in range(l+1,r+1):
                if nums[i] <= nums[l]:
                    nums[boundary_i],nums[i] = nums[i],nums[boundary_i]
                    boundary_i += 1

            boundary_i -= 1
            nums[l],nums[boundary_i] = nums[boundary_i],nums[l]
            cur_rank = boundary_i - l

            if cur_rank == rank: return nums[boundary_i]
            elif cur_rank < rank: return helper(boundary_i+1,r,l+rank - boundary_i - 1)
            else: return helper(l,boundary_i-1,rank)

        return helper(0,len(nums)-1,k)

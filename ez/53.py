# Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            current_max = max(current_max, nums[i])
        return current_max

        
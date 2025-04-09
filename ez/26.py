# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # 最初の要素を基準にする
        last_unique_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[last_unique_index]:
                last_unique_index += 1
                nums[last_unique_index] = nums[i]

        return last_unique_index + 1
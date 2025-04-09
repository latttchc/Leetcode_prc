# Remove Element
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 最初の要素を基準にする
        last_unique_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[last_unique_index] = nums[i]
                last_unique_index += 1

        return last_unique_index
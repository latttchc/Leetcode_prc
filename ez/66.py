class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):  # 末尾からスタート
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0  # 繰り上げが必要な場合

        # 全部繰り上がった場合（例: [9,9,9] → [1,0,0,0]）
        return [1] + digits

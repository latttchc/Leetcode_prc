# Roman to Integer
class Solution():
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0

        for char in s:
            value = roman[char]
            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value
        return total
    
        # ローマ数字を左から順に見ていき
        # 減算ルール（小→大の組み合わせ）を考慮しながら
        # 最終的に整数に変換する
# Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 1
        for _ in range(2, n + 1):
            first, second = second, first + second
        return second
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2))  # Output: 2
    print(solution.climbStairs(3))  # Output: 3
    print(solution.climbStairs(4))  # Output: 5
    print(solution.climbStairs(5))  # Output: 8
    print(solution.climbStairs(6))  # Output: 13
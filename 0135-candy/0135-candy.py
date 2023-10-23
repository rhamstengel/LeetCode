from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Initialize each child with at least one candy
        
        # First pass: Start from left to right, ensuring higher-rated children get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Second pass: Start from right to left, ensuring higher-rated children get more candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Calculate the total number of candies required
        total_candies = sum(candies)
        
        return total_candies

# Example usage
ratings1 = [1, 0, 2]
ratings2 = [1, 2, 2]

solution = Solution()
print(solution.candy(ratings1))  # Output: 5
print(solution.candy(ratings2))  # Output: 4

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Adding 1 to indices since the array is 1-indexed
            
            elif current_sum < target:
                left += 1
            
            else:
                right -= 1
        
        return []  # If no solution is found

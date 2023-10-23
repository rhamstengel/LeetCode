import random

class RandomizedSet:
    def __init__(self):
        self.nums = []  # List to store the inserted numbers
        self.num_to_index = {}  # Dictionary to store the mapping of numbers to their indices in the list

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False  # Value already exists in the set, no need to insert again
        
        self.nums.append(val)  # Append the value to the list
        self.num_to_index[val] = len(self.nums) - 1  # Store the index of the value in the dictionary
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False  # Value does not exist in the set, cannot remove
        
        index = self.num_to_index[val]  # Get the index of the value in the list
        
        # Swap the value with the last element in the list
        last_val = self.nums[-1]
        self.nums[index] = last_val
        self.num_to_index[last_val] = index
        
        # Remove the value from the list and dictionary
        self.nums.pop()
        del self.num_to_index[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

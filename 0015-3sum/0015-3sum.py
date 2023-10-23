class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array
        nums.sort()

        # Create an empty list to store the result
        res = []

        # Loop through each index in the array
        for i in range(len(nums)):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Use two pointers to find pairs that sum up to -nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res

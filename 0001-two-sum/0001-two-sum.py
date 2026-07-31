class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # Enumerate the list. x is the index, y is the value.
        # Example: nums = [1, 2, 3, 4], (x,y) = (0, 1), (1, 2), (2, 3), (3, 4)
        for x,y in enumerate(nums):
            difference = target - y # Calculate the difference. Example: 6 - 3 = 3
            if difference in seen:
                return [seen[difference], x] # If it's in seen, it would return the index of the difference in "seen" as well as the index of our list.
            seen[y] = x # If it's not in seen, add it to the dictionary.
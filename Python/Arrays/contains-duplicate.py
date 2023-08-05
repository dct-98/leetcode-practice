class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Proposed Solution:
        # Generate set of unique nums
        # Compare length of unique nums and nums
        # If they are not equal there is a duplicate number in nums

        unique_nums = set(nums)
        return len(unique_nums) != len(nums)
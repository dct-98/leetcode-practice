class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input
        #     nums:array of ints
        #     target:integer
        # Output
        #     indices:list
        # Proposed Solution
        #     Create dict
        #     Iterate through nums
        #         check if max(target - num, num - target) is in dict
        #             return index of both in list
        #         if not add value:index to dict

        nums_dict = {}

        for index in range(len(nums)):
            target_num = target - nums[index]
            if target_num in nums_dict:
                return [nums_dict[target_num], index]
            nums_dict[nums[index]] = index

        return []

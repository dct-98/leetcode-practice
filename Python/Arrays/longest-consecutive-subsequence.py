class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Inputs
        #   nums:list
        #       a list of numbers
        # Outputs
        #   longest:int
        #       an integer representing the length of the longest consecutive subsequence
        # Proposed Solution
        #   create set from nums
        #   iterate through each number in the set
        #   check if it is the beginning of a subsequence, it could not be if a number of n - 1 exists, but will
        #       for sure be one if it does not exist
        #   iterate through set checking if number + 1 is in the number set
        #   track and return longest length
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)


        return longest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        if n < 3:
            return []

        if nums[0] > 0 or nums[-1] < 0 or (nums[0] + nums[1] + nums[2] > 0) or (nums[-1] + nums[-2] + nums[-3] < 0):
            return result
        for i in range(n):
            # Avoiding duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total_sum < 0:
                    left += 1

                else:
                    right -= 1

        return result

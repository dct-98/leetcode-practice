class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        max_area = 0

        left = 0
        right = n - 1

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height

            if max_area < area:
                max_area = area
                continue

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
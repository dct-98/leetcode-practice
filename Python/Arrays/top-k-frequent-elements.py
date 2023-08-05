import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Could
        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        top_k = []
        for num, count in nums_dict.items():
            heapq.heappush(top_k, (count, num))
            if len(top_k) > k:
                heapq.heappop(top_k)

        return [num for counts, num in top_k]

# Solution without external libraries
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_dict = {}
#
#         for num in nums:
#             nums_dict[num] = nums_dict.get(num, 0) + 1
#
#         counts = [(num, count) for num, count in nums_dict.items()]
#         counts.sort(key=lambda x: x[1], reverse=True)
#
#         return [num for num, count in counts[:k]]

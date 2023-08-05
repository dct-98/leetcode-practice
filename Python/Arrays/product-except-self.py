class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Inputs
        #   nums:list
        #       list of numbers
        # Outputs
        #   products:list
        #       product of list, excluding i
        # Proposed Solution
        #   create a list of length of nums populating with 1
        #   iterate through nums starting at 1 to generate the products of list to the left
        #   iterate through product and nums generating right product and product of array except it's own index
        list_length = len(nums)
        products = [1 for _ in range(list_length)]

        for i in range(1, list_length):
            products[i] = nums[i - 1] * products[i - 1]

        right_products = 1

        for j in range(list_length - 1, -1, -1):
            products[j] *= right_products
            right_products *= nums[j]

        return products

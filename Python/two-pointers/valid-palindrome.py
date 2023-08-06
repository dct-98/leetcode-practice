class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Input
        #   s:string
        #       a string to check if it is a palindrome
        # Output
        #   is_palindrome:bool
        #       boolean indicating whether the string is a palindrome
        # Proposed Solution
        #   Scrapped
        #       remove all non-alphanumeric characters from string
        #   create left and right pointers
        #   Check if current index in string at left or right is not alphanumeric
        #   iterate through string until an inequality is found
        #   return false if found
        #   if not found return true

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Input:
        #     s:string
        #     t:string
        # Output:
        #     bool
        # Proposed Solution
        #     Initiate dict, letter:occurences from s
        #     Iterate through each char in t
        #         if not in dict table or occurences == 0
        #             return False
        #     if length of dict not equal to 0 return False
        #     else return True

        if len(s) != len(t):
            return False

        character_occurrences = {}

        for char in s:
            character_occurrences[char] = character_occurrences.get(char, 0) + 1

        for char in t:
            if character_occurrences.get(char, 0) == 0:
                return False
            character_occurrences[char] -= 1

        return all(value == 0 for value in character_occurrences.values())

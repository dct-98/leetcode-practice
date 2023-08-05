class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Inputs
        #   strs:array
        #       array of strings
        # Outputs
        #   unique_strs_array:array
        #       array of strings grouped into anagrams
        # Proposed Solution
        #   Create dictionary
        #   Iterate through strs
        #       Sort word,
        #       if sorted word is not in dictionary,
        #           add sorted word into dictionary with empty array as it's value
        #       add word into sorted word array
        #   return array of dictionary values
        
        unique_strs = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in unique_strs:
                unique_strs[sorted_word] = []
            unique_strs[sorted_word].append(word)

        return list(unique_strs.values())

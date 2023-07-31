/*
    Problem Description:
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.

    Examples:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {

    // Returns 0 if length of nums is 0
    if (nums.length === 0) return 0;

    // Create new Set from nums array
    let numSet = new Set(nums);
    let longest = 0;

    for (let num of nums) {

        // Checks if current num of nums is the start of a subsequence, if there is a number before it cannot be the start
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentLength = 1;
            

            // While the set has currentNum + 1, the subsequence will still continue.
            while(numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentLength += 1;
                
            }


            // Longest streak
            longest = Math.max(longest, currentLength);
        }
    }

    return longest;
    
};
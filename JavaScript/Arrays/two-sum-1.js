/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
    
    // Initialize map for num:index
    let numsIndex = {};

    for (let i = 0; i < nums.length; i++) {

        // Number to seek for
        let seekNum = target - nums[i];

        // If object has seekNum return seekNum:index , i
        if (numsIndex.hasOwnProperty(seekNum)) {
            return [numsIndex[seekNum], i];
        }

        numsIndex[nums[i]] = i;

    }
    return [];

};

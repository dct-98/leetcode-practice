/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let obj = {};


    // Counts the how often each number appears
    for (let num of nums) {
        obj[num] = (obj[num] || 0) + 1;
    }

    // Sort the keys based on their frequency
    // Slice 0,k elements

    return Object.keys(obj).sort((a,b) => obj[b] - obj[a]).slice(0, k).map(Number);
    

};

console.log(topKFrequent([1,1,1,2,2,3], 2))
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    const uniqueNums = new Set(nums);

    return uniqueNums.size !== nums.length;

};

console.log(containsDuplicate([1,2,3,1])); // True
console.log(containsDuplicate([1,2,3,4])); // False 
console.log(containsDuplicate([1,1,1,3,3,4,3,2,4,2])); //True

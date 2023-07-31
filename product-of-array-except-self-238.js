/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let length = nums.length;
    // Two arrays to keep track of products to the left and right of each number and result array to fill at the end
    let leftProduct = new Array(length).fill(1);
    let rightProduct = new Array(length).fill(1);
    let result = new Array(length);

    // Keeps track of all products to the left
    for(let i = 1; i < length; i++) {
        leftProduct[i] = nums[i - 1] * leftProduct[i - 1];
    }

    // Keeps track of all product the right
    for(let j = length - 2; j >= 0; j--) {
        rightProduct[j] = nums[j + 1] * rightProduct[j + 1];
    }

    // Combines all products into array
    for(let i = 0; i < length; i++) {
        result[i] = leftProduct[i] * rightProduct[i];
    }

    // Returns result
    return result;
};